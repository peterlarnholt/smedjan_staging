# Handled.sh - Final LP Deployment Instructions

## 🎯 A/B TEST STATUS: OPTION A (JAVASCRIPT) - LIVE

**Current Setup:**
- JavaScript A/B test is ALREADY RUNNING on handled.sh
- 50/50 cookie-based split with 1-year persistence
- Variant A (current): Main site at handled.sh/
- Variant B (new): /test/ directory

**This package = Variant B update**

## 📦 Package Contents

- **index.html** - Main landing page (research-backed, mobile-optimized, with logos)
- **10 sub-pages** - about, blog, business, contact, feedback, help, privacy, referral, security, terms
- **images/** - Handled logo + META Business Partner badge

## ✅ Deployment Steps for Option A (JavaScript A/B Test)

### 1. Upload to /test/ Directory
```bash
# Upload all HTML files to /test/ directory (NOT root)
/test/index.html          # New LP with logos
/test/about.html
/test/blog.html
/test/business.html
/test/contact.html
/test/feedback.html
/test/help.html
/test/privacy.html
/test/referral.html
/test/security.html
/test/terms.html

# Upload images to /test/images/ directory
/test/images/handled-logo.png
/test/images/meta-business-partner.png
```

**CRITICAL:** Do NOT touch the root directory - JavaScript split at root redirects to /test/ for variant B users.

### 2. Add Missing Assets (REQUIRED)
Upload to /test/ directory:

- **/test/favicon.svg** - Handled favicon
- **/test/og-image.jpg** - Open Graph image (1200x630px)
- **/test/twitter-card.jpg** - Twitter card image (1200x600px)

### 3. Verify JavaScript Split Still Works
After uploading to /test/:

1. Clear cookies for handled.sh
2. Visit handled.sh multiple times
3. Verify ~50% see variant A (current), ~50% redirected to /test/ (new)
4. Cookie `ab=a` or `ab=b` should persist for 1 year

### 4. Test Mobile Responsiveness (Variant B)
Test /test/index.html specifically:
- Test on iOS (Safari)
- Test on Android (Chrome)
- Verify logos scale properly:
  - Desktop: 40px logo / 50px META badge
  - Tablet (≤768px): 32px logo / 40px META badge  
  - Mobile (≤480px): 28px logo / 35px META badge

### 5. Verify All CTAs Work (Variant B)
All "Start Free" buttons in /test/ should link to: `https://handled.sh/whatsapp`

Make sure this URL is correct and functional.

### 6. Performance Check (Variant B)
Run Lighthouse audit on /test/index.html:
- Performance: Target 90+
- Accessibility: Target 95+
- Best Practices: Target 90+
- SEO: Target 95+

## 📊 A/B Test Tracking Setup

**Choose tracking method:**

### Option 1: GA4 (Recommended)
Add custom dimension "variant" (a/b) to all pageviews from /test/.

### Option 2: Meta Pixel
Add variant parameter to Meta Pixel events from /test/.

**See earlier conversation for complete tracking code.**

## 🎯 What's Included (Variant B Features)

### ✅ SEO/AEO/GEO Optimization
- Complete meta tags (title, description, keywords, author)
- Open Graph + Twitter Cards
- JSON-LD structured data (SoftwareApplication, FAQPage, Organization)
- Canonical URLs
- FAQ schema for AI search engines

### ✅ Mobile-First Design
- Responsive breakpoints: 768px, 480px
- Touch targets ≥48px
- Fast loading (<2s target)
- Single-column mobile layout

### ✅ Professional Branding
- Light mode only
- Purple theme (#8b5cf6)
- No emoji spam (only UI symbols)
- Handled logo + META Business Partner badge

### ✅ Contact & Pricing
- All emails → hello@handled.sh
- Free forever plan (unlimited tasks)
- Pro plan: $79/year
- No NordSym/Symbot/Molle branding

## 📊 Expected Results (After 2-4 Weeks)

Compare Variant A vs Variant B:
- Conversion rate (signups)
- Bounce rate
- Time on page
- CTR on "Start Free" button

**Winning variant gets deployed to root.**

## 🛠️ Quick Fixes Needed (from SEO audit)

**Week 1 Priority for Variant B:**
1. Add HowTo schema (2 hours) - Featured snippet opportunity
2. Fix H1 keyword targeting (30 min) - Better ranking
3. Add Product schema for Pro tier (2 hours) - Rich snippets

See full SEO report: `handled-seo-aeo-geo-analysis.md`

## ⚠️ DO NOT

- ❌ Upload to root (kills A/B test)
- ❌ Modify JavaScript split code
- ❌ Change cookie parameters
- ❌ Remove variant A (current site)

## 📞 Support

Questions? Contact:
- Molle: molle@nordsym.com
- Peter: peter@excom.ai

---

**Ready to deploy to /test/!** This updates Variant B in the live A/B test.
