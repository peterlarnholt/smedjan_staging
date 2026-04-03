#!/usr/bin/env python3
"""Generate hero image variants using DALL-E 3."""

import os
import base64
import httpx
from openai import OpenAI
from pathlib import Path

# Load key from handled-marketing .env
env_path = Path(__file__).resolve().parent.parent / "handled-marketing" / "onboarding-video" / ".env"
for line in env_path.read_text().splitlines():
    if line.startswith("OPENAI_API_KEY="):
        os.environ["OPENAI_API_KEY"] = line.split("=", 1)[1].strip()
        break

client = OpenAI()
out_dir = Path(__file__).resolve().parent / "docs" / "public"

# Style guide matching existing images
STYLE = (
    "Photorealistic editorial photograph, VERTICAL portrait orientation, "
    "warm golden hour lighting, shallow depth of field, cinematic color grading. "
    "The subject is using or holding a smartphone. Natural, candid feel — not posed or stocky. "
    "The person should be upright and vertical in the frame, shot in portrait mode. "
    "High-end lifestyle photography, shot on Sony A7IV with 85mm f/1.4 lens."
)

PROMPTS = [
    "A young woman sitting cross-legged on her suitcase in a crowded airport terminal, peacefully scrolling her phone with a gentle smile. Travelers rushing past in every direction as motion blur. Flight departure boards and large windows with golden sunlight streaming in behind her. She looks completely unbothered and calm. Cozy sweater, jeans, white sneakers. Her face is natural and relaxed with soft features.",

    "A young woman sitting cross-legged on her suitcase in a busy airport terminal, calmly looking at her phone. People walking past her in motion blur. Large windows with warm light, departure boards overhead. She wears a comfortable knit sweater and jeans. Peaceful expression, natural beauty, no makeup artifacts. The scene conveys calm amidst chaos.",

    "A young woman perched on her rolling suitcase in a bustling airport departure hall, scrolling her phone serenely. Rushing commuters blur around her. Sunlight pours through floor-to-ceiling windows. She wears a casual cozy outfit. Her face is lit softly by natural light, relaxed and content. Clean realistic skin and features.",

    "A young woman sitting casually on her luggage in a crowded airport gate area, absorbed in her phone with a slight smile. Motion-blurred travelers pass around her. Golden afternoon light from large terminal windows. Wearing a soft cardigan and comfortable travel clothes. Natural realistic facial features, soft lighting on her face.",
]

def generate(prompt: str, index: int):
    print(f"\n[{index}/{len(PROMPTS)}] Generating...")
    print(f"  Prompt: {prompt[:80]}...")

    resp = client.images.generate(
        model="dall-e-3",
        prompt=f"{prompt}\n\n{STYLE}",
        size="1024x1792",
        quality="hd",
        n=1,
    )

    image_url = resp.data[0].url
    revised_prompt = resp.data[0].revised_prompt
    print(f"  Revised: {revised_prompt[:100]}...")

    # Download
    img_data = httpx.get(image_url, timeout=60).content
    filename = f"g-hero-new-55-v{index}.jpg"
    filepath = out_dir / filename
    filepath.write_bytes(img_data)
    print(f"  Saved: {filepath.name} ({len(img_data) // 1024} KB)")
    return filepath


if __name__ == "__main__":
    print(f"Generating {len(PROMPTS)} hero image variants...")
    print(f"Output: {out_dir}\n")

    generated = []
    for i, prompt in enumerate(PROMPTS):
        try:
            path = generate(prompt, i + 1)
            generated.append(path)
        except Exception as e:
            print(f"  ERROR: {e}")

    print(f"\n--- Done! Generated {len(generated)}/{len(PROMPTS)} images ---")
    for p in generated:
        print(f"  {p.name}")
