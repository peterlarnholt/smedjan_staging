---
layout: home
markdownStyles: false
title: Support
description: "Get help with handled.sh. Contact our support team, browse FAQs, or troubleshoot common issues."
head:
  - - meta
    - property: og:title
      content: Support - handled.sh
  - - meta
    - property: og:description
      content: Get help with handled.sh. Contact our support team, browse FAQs, or troubleshoot common issues.
  - - meta
    - property: og:url
      content: https://handled.sh/support
  - - link
    - rel: canonical
      href: https://handled.sh/support

hero:
  name: Support
  text: We're Here to Help
  tagline: Get in touch or find answers to common questions.

---

<div class="support-content">

<section class="contact-section">

## Contact Us

<div class="contact-cards">
<div class="contact-card">
<h3>Email Support</h3>
<p>Send us a message and we'll get back to you within 24 hours.</p>
<a href="mailto:support@handled.sh" class="contact-cta">support@handled.sh</a>
</div>

<div class="contact-card">
<h3>General Inquiries</h3>
<p>Questions about pricing, partnerships, or anything else.</p>
<a href="mailto:contact@handled.sh" class="contact-cta">contact@handled.sh</a>
</div>
</div>

</section>

<section>

## Common Issues

<div class="faq-category">

<details>
<summary>My bot is not responding</summary>
<p>Try restarting your assistant from the <a href="https://handled.sh/dashboard" target="_self">dashboard</a> using the "Restart" button. If the issue persists, disconnect and reconnect your messaging app.</p>
</details>

<details>
<summary>My integration stopped working</summary>
<p>Integration tokens can expire. Go to your <a href="https://handled.sh/dashboard" target="_self">dashboard</a>, disconnect the integration, and reconnect it. This refreshes the authorization.</p>
</details>

<details>
<summary>Messages are delayed</summary>
<p>Short delays (a few seconds) are normal — your assistant is thinking and working on your request. If delays are consistently long, try restarting your assistant from the dashboard.</p>
</details>

<details>
<summary>I'm not receiving reminders</summary>
<p>Make sure your messaging app (WhatsApp or Telegram) is connected and showing as "Online" on the dashboard. Also check that your assistant knows your timezone — you can tell it or send a location pin.</p>
</details>

<details>
<summary>How do I cancel my subscription?</summary>
<p>You can manage or cancel your subscription at any time from the <a href="https://handled.sh/dashboard" target="_self">dashboard</a>. Tap "Manage" on your subscription banner, and you'll be taken to the billing portal.</p>
</details>

<details>
<summary>How do I delete my account and data?</summary>
<p>Visit our <a href="/data-deletion">data deletion page</a> for instructions on how to request complete deletion of your account and all associated data.</p>
</details>

</div>

</section>

<section>

## More Resources

<div class="resource-cards">
<a href="/help" class="resource-card">
<h3>Help Center</h3>
<p>Browse FAQs and step-by-step guides for getting started, integrations, and features.</p>
</a>

<a href="/privacy" class="resource-card">
<h3>Privacy Policy</h3>
<p>Learn how we handle your data and protect your privacy.</p>
</a>

<a href="/security" class="resource-card">
<h3>Security</h3>
<p>Details on our security practices, encryption, and data isolation.</p>
</a>

<a href="/terms" class="resource-card">
<h3>Terms of Service</h3>
<p>Our terms and conditions for using handled.sh.</p>
</a>
</div>

</section>

</div>

<style>
.support-content {
  max-width: 1152px;
  margin: 0 auto;
  padding: 0 24px;
}

@media (min-width: 640px) {
  .support-content { padding: 0 48px; }
}

@media (min-width: 960px) {
  .support-content { padding: 0 64px; }
}

.support-content section {
  padding: 2rem 0;
}

.support-content section + section {
  border-top: 1px solid var(--vp-c-border);
}

.support-content h2 {
  font-size: 1.4rem;
  font-family: 'Exo', sans-serif;
  margin: 0 0 1.5rem;
  letter-spacing: -0.02em;
}

.support-content h3 {
  font-size: 1.1rem;
  font-family: 'Exo', sans-serif;
  color: var(--vp-c-text-1);
  margin: 0 0 0.75rem;
}

.support-content p {
  margin: 0;
}

/* Contact cards */
.contact-cards {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

@media (max-width: 640px) {
  .contact-cards { grid-template-columns: 1fr; }
}

.contact-card {
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-border);
  border-radius: 12px;
  padding: 1.5rem;
  text-align: center;
}

.contact-card:hover {
  border-color: var(--vp-c-brand-2);
  box-shadow: 0 0 20px rgba(139, 92, 246, 0.1);
}

.contact-card p {
  color: var(--vp-c-text-2);
  font-size: 0.9rem;
  margin-bottom: 1.25rem !important;
}

.contact-cta {
  display: inline-block;
  padding: 0.6rem 2rem;
  background: #8b5cf6;
  color: #fff !important;
  text-decoration: none !important;
  border-radius: 8px;
  font-weight: 600;
  transition: all 0.2s;
}

.contact-cta:hover {
  background: #7c3aed;
  box-shadow: 0 0 20px rgba(139, 92, 246, 0.4);
  transform: translateY(-1px);
}

/* FAQ items */
.faq-category {
  margin-bottom: 0;
}

.faq-category details {
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-border);
  border-radius: 10px;
  margin-bottom: 0.5rem;
  transition: border-color 0.2s;
}

.faq-category details:hover {
  border-color: var(--vp-c-brand-2);
}

.faq-category details[open] {
  border-color: var(--vp-c-brand-2);
  box-shadow: 0 0 12px rgba(139, 92, 246, 0.08);
}

.faq-category summary {
  padding: 0.85rem 1.25rem;
  cursor: pointer;
  font-weight: 600;
  font-size: 0.95rem;
  color: var(--vp-c-text-1);
  list-style: none;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.5rem;
}

.faq-category summary::-webkit-details-marker {
  display: none;
}

.faq-category summary::after {
  content: "+";
  font-size: 1.2rem;
  color: var(--vp-c-text-3);
  flex-shrink: 0;
  transition: transform 0.2s;
}

.faq-category details[open] summary::after {
  content: "\2212";
  color: #a78bfa;
}

.faq-category details p {
  padding: 0 1.25rem 1rem;
  color: var(--vp-c-text-2);
  font-size: 0.9rem;
  line-height: 1.6;
}

.faq-category details a {
  color: #a78bfa;
  text-decoration: underline;
  text-underline-offset: 2px;
}

.faq-category details a:hover {
  color: #c4b5fd;
}

/* Resource cards */
.resource-cards {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

@media (max-width: 640px) {
  .resource-cards { grid-template-columns: 1fr; }
}

.resource-card {
  display: block;
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-border);
  border-radius: 12px;
  padding: 1.25rem;
  text-decoration: none !important;
  transition: all 0.2s;
}

.resource-card:hover {
  border-color: var(--vp-c-brand-2);
  box-shadow: 0 0 20px rgba(139, 92, 246, 0.1);
  transform: translateY(-1px);
}

.resource-card h3 {
  color: var(--vp-c-text-1) !important;
}

.resource-card p {
  color: var(--vp-c-text-2);
  font-size: 0.85rem;
  line-height: 1.5;
}

@media (max-width: 768px) {
  .faq-category summary {
    font-size: 0.9rem;
    padding: 0.75rem 1rem;
  }
  .faq-category details p {
    padding: 0 1rem 0.85rem;
  }
}
</style>
