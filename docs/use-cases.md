---
layout: home
markdownStyles: false
title: Who Is It For?
description: "handled.sh works for everyone: students, parents, freelancers, executives, travelers, and anyone who wants a personal productivity assistant on WhatsApp."
head:
  - - meta
    - property: og:title
      content: Who Is It For? - handled.sh
  - - meta
    - property: og:description
      content: "Students, parents, freelancers, executives, travelers. See how handled.sh fits your life."
  - - meta
    - property: og:url
      content: https://handled.sh/use-cases
  - - link
    - rel: canonical
      href: https://handled.sh/use-cases

hero:
  name: Who Is It For?
  text: Whatever Your Day Looks Like, It's Handled.
  tagline: See how people like you use their productivity assistant every day.
  actions:
    - theme: brand
      text: Get Started
      link: https://app.handled.sh/dashboard
      target: _self

---

<div class="page-content uc-content">

<section>

<div class="uc-grid">

<div class="uc-card">
<div class="uc-emoji">👔</div>
<h3>Busy Professionals</h3>
<ul>
<li>"I'm double-booked Thursday afternoon, reschedule the less urgent one and email them"</li>
<li>"Check my inbox and flag anything urgent from the last 6 hours"</li>
<li>"Prep me for my 2pm — pull the agenda, attendees, and any docs they shared"</li>
<li>"Move my 3pm to tomorrow and email the attendees"</li>
<li>"Every Monday at 7am send me my week ahead: meetings, deadlines, and open tasks"</li>
</ul>
</div>

<div class="uc-card">
<div class="uc-emoji">🔧</div>
<h3>Freelancers & Business Owners</h3>
<ul>
<li>"Email the client a payment reminder — the invoice is 14 days overdue"</li>
<li>"Schedule a follow-up email to 'hello@acme.co' for next Tuesday at 9am"</li>
<li>"Send me a weekly report of all unpaid invoices every Friday at 4pm"</li>
<li>"Find me tickets for the Arsenal game next Saturday"</li>
<li>"Track my competitor's pricing page and alert me if anything changes"</li>
</ul>
</div>

<div class="uc-card">
<div class="uc-emoji">🎓</div>
<h3>Students</h3>
<ul>
<li>"Build me a study schedule around my classes for exam week"</li>
<li>"How many free hours do I have between lectures this week?"</li>
<li>"Remind me about the biology exam on March 12 — and 3 days before to start reviewing"</li>
<li>"Block 2 hours every evening this week for thesis writing"</li>
<li>"Remind me about the group project meeting every Wednesday at 2pm"</li>
</ul>
</div>

<div class="uc-card">
<div class="uc-emoji">👩‍👧‍👦</div>
<h3>Parents & Families</h3>
<ul>
<li>"Monitor Hemnet for 3-bedroom apartments in Södermalm under 5M SEK"</li>
<li>"Alert me when new listings pop up on Rightmove in East London"</li>
<li>"Remind me to pick up the kids at 3pm"</li>
<li>"Add dentist appointment on Thursday at 10"</li>
<li>"Remind me about our anniversary on June 15"</li>
</ul>
</div>

<div class="uc-card">
<div class="uc-emoji">✈️</div>
<h3>Travelers & Expats</h3>
<ul>
<li>"Track CPH to BCN flights and alert me on price drops"</li>
<li>"Find the cheapest day to fly to New York in June"</li>
<li>"Notify me if my EK 840 flight schedule changes"</li>
<li>"Book a table for 2 at Nobu on Saturday at 8pm"</li>
<li>"What's on my calendar tomorrow and do I have any conflicts?"</li>
</ul>
</div>

<div class="uc-card">
<div class="uc-emoji">📡</div>
<h3>Investors & Deal Hunters</h3>
<ul>
<li>"Track my portfolio and notify me if any position moves more than 5%"</li>
<li>"Alert me if Tesla drops below $180"</li>
<li>"Track Bitcoin and notify me daily at 9am"</li>
<li>"Watch this TV and alert me if the price drops"</li>
<li>"Notify me when EUR/USD crosses 1.10"</li>
</ul>
</div>

</div>

</section>

<section class="uc-cta-section">

## Sound Like You?

<p class="uc-cta-text">Free forever. No credit card. Just message your productivity assistant.</p>
<a href="https://app.handled.sh/dashboard" target="_self" class="cta-btn">Get Started</a>

</section>

</div>

<style>
/* Use case cards */
.uc-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}

.uc-card {
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-border);
  border-radius: 12px;
  padding: 1.5rem;
}

.uc-card:hover {
  border-color: var(--vp-c-brand-2);
  box-shadow: 0 0 20px rgba(139, 92, 246, 0.1);
}

.uc-emoji {
  font-size: 2rem;
  margin-bottom: 0.5rem;
}

.uc-card h3 {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--vp-c-text-1);
  margin: 0 0 0.75rem;
  font-family: 'Exo', sans-serif;
}

.uc-card ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.uc-card li {
  padding: 0.3rem 0;
  color: var(--vp-c-text-2);
  font-size: 0.85rem;
  line-height: 1.5;
  font-style: italic;
}

.uc-card li::before {
  content: "\203A  ";
  color: #8b5cf6;
  font-style: normal;
  font-weight: 700;
}

/* CTA */
.uc-cta-section {
  text-align: center;
}

.uc-cta-text {
  color: var(--vp-c-text-2);
  font-size: 1rem;
  margin: 0 0 1.5rem;
}

/* Responsive */
@media (max-width: 960px) {
  .uc-grid { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 640px) {
  .uc-grid { grid-template-columns: 1fr; }
}
</style>
