"""Generate Teams-style mockup screenshots for the app store listing."""
from playwright.sync_api import sync_playwright
import json, os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

SCENARIOS = [
    {
        "filename": "01-calendar.png",
        "messages": [
            {"role": "user", "text": "What's on my calendar today?"},
            {"role": "bot", "text": "Here's your schedule for today (Monday, March 1):\n\n\u2022 9:00 AM \u2013 Team standup (Google Meet)\n\u2022 11:30 AM \u2013 Lunch with Sarah @ Cafe Milano\n\u2022 2:00 PM \u2013 Product review (Room 3B)\n\u2022 4:30 PM \u2013 1:1 with manager\n\nYou have a 2-hour gap between 9:30 and 11:30. Want me to block focus time there?"},
            {"role": "user", "text": "Yes, block 10\u201311:30 as focus time"},
            {"role": "bot", "text": "Done \u2014 I've added \"Focus time\" to your calendar from 10:00 to 11:30 AM. I marked it as busy so you won't get meeting invites during that window."},
        ]
    },
    {
        "filename": "02-email.png",
        "messages": [
            {"role": "user", "text": "Send an email to sarah@company.com about rescheduling our Friday meeting to next Monday"},
            {"role": "bot", "text": "I've drafted this email:\n\n\u2014\u2014\u2014\nTo: sarah@company.com\nSubject: Rescheduling Friday meeting\n\nHi Sarah,\n\nWould it work for you to move our Friday meeting to Monday instead? Same time works for me, but I'm flexible if you'd prefer a different slot.\n\nLet me know!\n\u2014\u2014\u2014\n\nShall I send it?"},
            {"role": "user", "text": "Looks good, send it"},
            {"role": "bot", "text": "Sent! I'll let you know if Sarah replies."},
        ]
    },
    {
        "filename": "03-reminders.png",
        "messages": [
            {"role": "user", "text": "Remind me every weekday at 8:45 AM to check my calendar before standup"},
            {"role": "bot", "text": "Got it! I've set a recurring reminder:\n\n\u23F0 Every weekday at 8:45 AM\n\"Check your calendar before standup\"\n\nI'll also include your schedule for the day in the reminder so you're fully prepared. You can say \"cancel the standup reminder\" anytime to stop it."},
            {"role": "user", "text": "Also remind me to submit the Q1 report by March 15"},
            {"role": "bot", "text": "Done \u2014 I'll remind you on March 15 to submit the Q1 report. Want me to remind you a few days early too, so you have time to prepare?"},
            {"role": "user", "text": "Yes, also on March 12"},
            {"role": "bot", "text": "Perfect. You'll get two reminders:\n\u2022 March 12 \u2014 \"Q1 report due in 3 days\"\n\u2022 March 15 \u2014 \"Submit Q1 report today\""},
        ]
    },
    {
        "filename": "04-tasks.png",
        "messages": [
            {"role": "user", "text": "Add these to my Todoist: buy groceries, call dentist, and review the presentation"},
            {"role": "bot", "text": "Added 3 tasks to your Todoist inbox:\n\n\u2705 Buy groceries\n\u2705 Call dentist\n\u2705 Review the presentation\n\nWant me to set due dates or priorities for any of these?"},
            {"role": "user", "text": "Set the presentation review as high priority, due tomorrow"},
            {"role": "bot", "text": "Updated! \"Review the presentation\" is now priority 1 (high) and due tomorrow, March 2. I'll remind you in the morning."},
        ]
    },
    {
        "filename": "05-research.png",
        "messages": [
            {"role": "user", "text": "Find me the best rated Italian restaurants near Dubai Marina that are open tonight"},
            {"role": "bot", "text": "Here are the top-rated Italian restaurants near Dubai Marina open tonight:\n\n1. \u2B50 Bussola (4.6) \u2014 Westin Dubai Mina Seyahi\n   Open until 11:30 PM \u2022 $$$\n\n2. \u2B50 BiCE Mare (4.5) \u2014 Souk Al Bahar\n   Open until 12:00 AM \u2022 $$$$\n\n3. \u2B50 Massimo's (4.4) \u2014 JBR Walk\n   Open until 11:00 PM \u2022 $$\n\nWant me to add a dinner reservation to your calendar or get directions to any of these?"},
            {"role": "user", "text": "Add dinner at BiCE Mare at 8pm to my calendar"},
            {"role": "bot", "text": "Done! Added to your calendar:\n\n\uD83C\uDF7D\uFE0F Dinner at BiCE Mare\nTonight, 8:00 PM\nSouk Al Bahar, Downtown Dubai\n\nEnjoy your dinner!"},
        ]
    },
]

HTML_TEMPLATE = open(os.path.join(SCRIPT_DIR, "mockup.html")).read()

def build_chat_html(messages):
    html_parts = []
    html_parts.append('<div class="date-divider">Today</div>')

    times = ["9:01 AM", "9:01 AM", "9:02 AM", "9:02 AM", "9:03 AM", "9:03 AM"]

    for i, msg in enumerate(messages):
        t = times[i] if i < len(times) else "9:04 AM"
        if msg["role"] == "user":
            html_parts.append(f'''
            <div>
                <div class="user-time">{t}</div>
                <div class="bubble user-bubble">{msg["text"]}</div>
            </div>''')
        else:
            text = msg["text"].replace("\n", "<br>")
            html_parts.append(f'''
            <div class="msg-row">
                <div class="avatar">&#10004;</div>
                <div class="msg-content">
                    <div class="sender-info">
                        <span class="sender-name">Handled</span>
                        <span class="msg-time">{t}</span>
                    </div>
                    <div class="bubble bot">{text}</div>
                </div>
            </div>''')

    return "\n".join(html_parts)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    for scenario in SCENARIOS:
        page = browser.new_page(viewport={"width": 1366, "height": 768})

        chat_html = build_chat_html(scenario["messages"])
        full_html = HTML_TEMPLATE.replace('<div class="chat" id="chat">\n</div>',
                                          f'<div class="chat" id="chat">\n{chat_html}\n</div>')

        page.set_content(full_html)
        page.wait_for_timeout(500)

        path = os.path.join(OUTPUT_DIR, scenario["filename"])
        page.screenshot(path=path)
        print(f"Saved: {path}")
        page.close()

    browser.close()

print(f"\nDone! {len(SCENARIOS)} screenshots saved to {OUTPUT_DIR}")
