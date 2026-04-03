---
title: Privacy Policy
description: "handled.sh privacy policy. Your data stays private: isolated environments, encrypted tokens, no AI training on your conversations."
head:
  - - meta
    - property: og:title
      content: Privacy Policy - handled.sh
  - - meta
    - property: og:description
      content: "Your data stays private: isolated environments, encrypted tokens, no AI training on your conversations."
  - - meta
    - property: og:url
      content: https://handled.sh/privacy
  - - link
    - rel: canonical
      href: https://handled.sh/privacy
---

# Privacy Policy

**Last updated:** February 27, 2026

handled.sh ("we", "us", "our") operates the handled.sh personal productivity assistant service, available at [https://handled.sh](https://handled.sh). This privacy policy describes what data we collect, how we use it, who we share it with, and how we protect it.

## Information We Collect

### Account Information
When you sign up, we collect your name, email address, and profile picture from your authentication provider (Google or Microsoft). This is used to create and manage your account.

### Messaging Data
When you interact with our assistant via Telegram, WhatsApp, or Microsoft Teams, we process the messages you send and receive. This includes your phone number (for WhatsApp), text messages, voice messages, commands, and any files or links you share with the assistant.

### Google User Data
When you connect Google services through our dashboard, we access the following data:

- **Google Calendar:** Your calendar events, including event titles, times, locations, descriptions, and attendees. We access this data to read, create, update, and delete events on your behalf when you ask your assistant to manage your calendar.
- **Gmail:** We access Gmail to send emails on your behalf, and to read, search, and summarize your email messages when you explicitly ask your assistant to do so. Email content is fetched in real time, processed, and not permanently stored.

We only request the minimum permissions (OAuth scopes) needed for each service to function. We access your Google data only when you explicitly ask your assistant to perform a task that requires it.

### Microsoft User Data
When you connect Microsoft services, we access:

- **Microsoft Calendar:** Your calendar events, to read and manage your schedule on your behalf.
- **Outlook Mail:** Your email messages, to read, summarize, and send emails on your behalf.

### Other Connected Services
- **Todoist:** Your tasks and projects, to create, complete, and manage tasks on your behalf.
- **WhatsApp, Telegram, and Microsoft Teams:** Your messages to and from the assistant, to provide the service.

### Usage Data
We collect basic usage data such as login timestamps, feature usage events, and error logs to operate and improve the service.

## How We Use Your Data

- **To provide the service:** Process your messages, execute the tasks you request, and deliver responses through your connected messaging platforms.
- **To fulfill integration requests:** When you ask your assistant to check your calendar, send an email, or manage tasks, we access the relevant connected service to carry out that specific request.
- **To improve the service:** Analyze anonymized usage patterns and fix issues. We do not use your messages, Google user data, or connected service data to train AI models.
- **To communicate with you:** Send service-related notifications.

**We do not use Google user data for serving advertisements, and we do not use it for any purpose other than providing and improving the handled.sh service.**

## Data Sharing and Disclosure

### AI Processing
Your messages and relevant context (such as calendar events or task lists you ask about) are sent to AI model providers to generate responses and complete tasks. This processing is strictly necessary to provide the service. We currently use Anthropic (Claude) and OpenAI (Whisper for voice transcription, text-to-speech for voice replies), and may add additional providers in the future. These providers do not use your data to train AI models when accessed via their APIs. See [Anthropic's privacy policy](https://www.anthropic.com/privacy) and [OpenAI's privacy policy](https://openai.com/privacy).

### We Do Not Sell Your Data
We do not sell, rent, license, or trade your personal data or Google user data to any third party.

### We Do Not Share Google User Data Beyond What Is Necessary
Google user data is only shared with AI model providers to the extent necessary to fulfill your specific requests. For example, if you ask "What's on my calendar today?", your calendar events for that day are sent to the AI model to generate a response. No Google user data is shared with any other third party.

### Other Disclosures
We may disclose your data only if required by law, such as in response to a valid legal process.

## Data Storage and Security

- All data is stored on Google Cloud Platform infrastructure with encryption at rest.
- All authentication tokens (Google, Microsoft, Todoist) are encrypted at rest and stored per-account with minimum required permissions.
- All data transmission uses HTTPS/TLS encryption.
- Each user's assistant runs in a completely isolated container environment. No other user can access your data, messages, or credentials.
- Access to production systems is restricted to authorized personnel using multi-factor authentication.
- We conduct regular security reviews of our infrastructure and access controls.

## Data Retention

We enforce specific retention periods for each category of data. Automated cleanup processes run daily within each user's isolated container to enforce these limits.

| Data type | Retention period |
|-----------|-----------------|
| **Conversation history** | Retained for up to **90 days**, then automatically deleted. |
| **Scheduled jobs** | One-time jobs are deleted immediately after execution. Recurring jobs persist until you delete them. |
| **Media files** (photos, documents, voice messages) | Processed and automatically deleted within **24 hours**. |
| **Memory file** (your preferences and context) | Retained while your account is active. Deleted on account deletion. |
| **Account data** (name, email, profile) | Retained while your subscription is active. Deleted within **30 days** of account deletion. |
| **Integration tokens** (Google, Microsoft, Todoist) | Deleted **immediately** on disconnection or account deletion. |
| **Google user data** (calendar events, email content) | Not permanently stored. Fetched in real time, processed, and not retained after the response is delivered. |
| **Microsoft user data** (calendar events, email content) | Same as Google user data — fetched in real time, not permanently stored. |
| **Usage data** (login timestamps, feature events) | Retained for up to **12 months** for analytics. Does not contain message content or connected service data. |

## Data Deletion

You can disconnect any integration at any time from your [dashboard](https://handled.sh/dashboard). You can delete your account and all associated data from your dashboard settings. Account deletion removes your Firestore user record, container, stored files, and all connected service tokens. Deletion completes within minutes.

## Your Rights

You have the right to:

- **Access** the personal data we hold about you.
- **Correct** inaccurate personal data.
- **Delete** your account and all associated data.
- **Disconnect** any third-party service at any time from your dashboard, which immediately removes stored tokens.
- **Export** your data upon request.
- **Revoke access** to Google services at any time via your [Google Account permissions](https://myaccount.google.com/permissions).

## Children's Privacy

Our service is not intended for use by anyone under the age of 16. We do not knowingly collect personal data from children.

## Changes to This Policy

We may update this privacy policy from time to time. If we make changes to how we use Google user data, we will notify you by email before those changes take effect. The "Last updated" date at the top reflects the most recent revision.

## Contact Us

If you have questions about this privacy policy or how your data is handled, please contact us at:

**Email:** [contact@handled.sh](mailto:contact@handled.sh)
