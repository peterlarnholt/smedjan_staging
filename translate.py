#!/usr/bin/env python3
"""Translate VitePress markdown files to multiple languages using Claude API."""

import os
import sys
import shutil
from pathlib import Path

try:
    import anthropic
except ImportError:
    print("Install the Anthropic SDK: pip install anthropic")
    sys.exit(1)

# Languages to translate to (code -> display name, native name)
LANGUAGES = {
    "es": ("Spanish", "Español"),
    "de": ("German", "Deutsch"),
    "pt": ("Portuguese", "Português"),
    "fr": ("French", "Français"),
    "ar": ("Arabic", "العربية"),
    "sv": ("Swedish", "Svenska"),
    "ru": ("Russian", "Русский"),
}

# Files to translate (relative to docs/)
CONTENT_FILES = [
    "index.md",
    "how-it-works.md",
    "pricing.md",
    "use-cases.md",
    "referral.md",
    "security.md",
    "privacy.md",
    "terms.md",
    "help.md",
]

DOCS_DIR = Path(__file__).parent / "docs"

SYSTEM_PROMPT = """You are a professional translator for a marketing website. Translate the given VitePress markdown file to {language}.

Rules:
- Translate ALL human-readable text (headings, paragraphs, button labels, descriptions, alt text, meta descriptions, FAQ answers)
- Keep the brand name "handled.sh" unchanged everywhere
- Keep ALL markdown syntax, HTML tags, CSS classes, frontmatter keys, and structure exactly as-is
- Keep all URLs, links, image paths, and hrefs unchanged
- Keep frontmatter YAML keys unchanged (only translate their string values)
- Keep JSON-LD structured data values translated but keys unchanged
- Keep code blocks and technical terms unchanged
- Keep SVG paths/elements unchanged
- For Arabic: the site layout handles RTL automatically, just translate the text
- The translation should feel natural and native, not literal, adapt marketing copy to sound compelling in {language}
- Return ONLY the translated file content, no explanations or markdown code fences"""


def translate_file(client: anthropic.Anthropic, content: str, language: str) -> str:
    """Translate a single markdown file using Claude."""
    response = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=16000,
        system=SYSTEM_PROMPT.format(language=language),
        messages=[{"role": "user", "content": content}],
    )
    return response.content[0].text


def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Set ANTHROPIC_API_KEY environment variable")
        sys.exit(1)

    # Allow filtering: python translate.py es sv
    target_langs = sys.argv[1:] if len(sys.argv) > 1 else list(LANGUAGES.keys())
    for lang in target_langs:
        if lang not in LANGUAGES:
            print(f"Unknown language: {lang}. Available: {', '.join(LANGUAGES.keys())}")
            sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    for lang_code in target_langs:
        lang_name, native_name = LANGUAGES[lang_code]
        lang_dir = DOCS_DIR / lang_code
        lang_dir.mkdir(exist_ok=True)

        print(f"\n{'='*50}")
        print(f"Translating to {lang_name} ({native_name}) -> docs/{lang_code}/")
        print(f"{'='*50}")

        for filename in CONTENT_FILES:
            src = DOCS_DIR / filename
            dst = lang_dir / filename

            if not src.exists():
                print(f"  SKIP {filename} (not found)")
                continue

            print(f"  Translating {filename}...", end=" ", flush=True)
            content = src.read_text(encoding="utf-8")
            translated = translate_file(client, content, lang_name)
            dst.write_text(translated, encoding="utf-8")
            print("OK")

    print(f"\nDone! Translated {len(target_langs)} language(s).")
    print("Run 'npm run dev' to preview, then 'npm run build' to build.")


if __name__ == "__main__":
    main()
