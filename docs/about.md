---
layout: home
markdownStyles: false
title: About
description: "handled.sh is a personal productivity assistant that connects to your real tools and takes real actions. Built for privacy, designed for people who get things done."
head:
  - - meta
    - property: og:title
      content: About - handled.sh
  - - meta
    - property: og:description
      content: "handled.sh is a personal productivity assistant that connects to your real tools and takes real actions. Built for privacy, designed for people who get things done."
  - - meta
    - property: og:url
      content: https://handled.sh/about
  - - link
    - rel: canonical
      href: https://handled.sh/about

hero:
  name: About
  text: Built for People Who Get Things Done
  tagline: We believe technology should work for you, not the other way around.

---

<div class="security-content">

<section>

## The Problem

Most assistants today are chatbots. They answer questions, but they don't take action. You still have to switch between apps, copy-paste information, and manage everything yourself. The promise was a personal productivity assistant — what we got was a search engine you can talk to.

</section>

<section>

## What We Built

handled.sh is a personal productivity assistant that connects to your real tools and takes real actions. It manages your calendar, sends emails, tracks prices, and reaches out to you first — with reminders, alerts, and daily briefings. You don't open an app to use it. You just send a message on WhatsApp or Telegram, and things get done.

</section>

<section>

## Privacy by Design

Every user gets their own private environment. Your data never touches anyone else's. No shared databases, no training on your conversations, no profiling. We believe privacy isn't a feature — it's a right. <a href="/security">Read more about our security model</a>.

</section>

<section>

## Company

handled.sh is a product of EXCOM AI L.L.C-FZ, a company registered in Dubai, United Arab Emirates. We build AI-powered productivity tools that connect to your real workflows and take real actions on your behalf.

</section>

<section>

## Get in Touch

Have questions, feedback, or just want to say hello? Reach us at <a href="mailto:contact@handled.sh">contact@handled.sh</a>. You can also visit our <a href="/help">Help Center</a> for guides and answers to common questions.

</section>

</div>

<style>
/* Reuses .security-content styles from security.md — VitePress deduplicates them */
.security-content {
  max-width: 1152px;
  margin: 0 auto;
  padding: 0 24px;
}

@media (min-width: 640px) {
  .security-content { padding: 0 48px; }
}

@media (min-width: 960px) {
  .security-content { padding: 0 64px; }
}

.security-content section {
  padding: 2rem 0;
}

.security-content section + section {
  border-top: 1px solid var(--vp-c-border);
}

.security-content h2 {
  font-size: 1.4rem;
  font-family: 'Exo', sans-serif;
  margin: 0 0 1.5rem;
  letter-spacing: -0.02em;
}

.security-content p {
  color: var(--vp-c-text-2);
  font-size: 0.95rem;
  line-height: 1.7;
  margin: 0;
}

.security-content a {
  color: #a78bfa;
  text-decoration: underline;
  text-underline-offset: 2px;
}

.security-content a:hover {
  color: #c4b5fd;
}
</style>
