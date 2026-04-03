<script setup>
import DefaultTheme from 'vitepress/theme'
import { onMounted, ref } from 'vue'
import { useData, useRouter } from 'vitepress'

const { Layout } = DefaultTheme
const { lang } = useData()
const router = useRouter()
const showBanner = ref(false)

const SUPPORTED_LOCALES = ['es', 'de', 'fr', 'pt', 'ar', 'sv']
const LOCALE_KEY = 'preferred-locale'

function acceptCookies() {
  localStorage.setItem('cookie-consent', 'accepted')
  showBanner.value = false
  loadAnalytics()
}

function declineCookies() {
  localStorage.setItem('cookie-consent', 'declined')
  showBanner.value = false
}

function loadAnalytics() {
  if (document.querySelector('script[src*="googletagmanager"]')) return
  const s = document.createElement('script')
  s.async = true
  s.src = 'https://www.googletagmanager.com/gtag/js?id=G-XXLGWW1JSV'
  document.head.appendChild(s)
  window.dataLayer = window.dataLayer || []
  function gtag() { window.dataLayer.push(arguments) }
  gtag('js', new Date())
  gtag('config', 'G-XXLGWW1JSV')

  // Microsoft Clarity
  if (!document.querySelector('script[src*="clarity.ms"]')) {
    ;(function(c,l,a,r,i,t,y){
      c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)}
      t=l.createElement(r);t.async=1;t.src='https://www.clarity.ms/tag/'+i
      y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y)
    })(window,document,'clarity','script','w2vh7gs076')
  }
}

onMounted(() => {
  // --- Locale auto-detection (first visit only) ---
  const path = window.location.pathname
  const currentLocale = SUPPORTED_LOCALES.find(l => path.startsWith(`/${l}/`) || path === `/${l}`) || 'en'
  const stored = localStorage.getItem(LOCALE_KEY)

  if (!stored) {
    // First visit: detect browser language and redirect if we have a match
    const browserLang = (navigator.language || '').split('-')[0].toLowerCase()
    if (browserLang && browserLang !== 'en' && SUPPORTED_LOCALES.includes(browserLang) && currentLocale === 'en') {
      localStorage.setItem(LOCALE_KEY, browserLang)
      // Redirect: / -> /es/, /privacy -> /es/privacy, etc.
      const newPath = `/${browserLang}${path === '/' ? '/' : path}`
      router.go(newPath)
      return
    }
    localStorage.setItem(LOCALE_KEY, 'en')
  } else if (currentLocale !== stored) {
    // User navigated to a different locale (via language switcher) — update preference
    localStorage.setItem(LOCALE_KEY, currentLocale)
  }

  // Force all app.handled.sh links to open in the same tab + pass language, UTMs, and ref
  const pageParams = new URLSearchParams(window.location.search)
  document.addEventListener('click', (e) => {
    const link = e.target.closest('a[href*="app.handled.sh"]')
    if (!link) return
    if (!link.hasAttribute('target')) {
      link.setAttribute('target', '_self')
    }
    const locale = lang.value?.split('-')[0] || 'en'
    try {
      const url = new URL(link.href)
      if (!url.searchParams.has('lang')) {
        url.searchParams.set('lang', locale)
      }
      // Forward UTM params and ref from the landing page
      for (const [key, val] of pageParams) {
        if ((key.startsWith('utm_') || key === 'ref') && !url.searchParams.has(key)) {
          url.searchParams.set(key, val)
        }
      }
      link.href = url.toString()
    } catch {}
  })

  // Cookie consent
  const consent = localStorage.getItem('cookie-consent')
  if (consent === 'accepted') {
    loadAnalytics()
  } else if (!consent) {
    showBanner.value = true
  }
})
</script>

<template>
  <Layout>
    <template #not-found>
      <div class="not-found">
        <p class="code">404</p>
        <h1>Page not found</h1>
        <p class="desc">The page you're looking for doesn't exist or has been moved.</p>
        <a href="/" class="home-link">Go to homepage</a>
      </div>
    </template>
  </Layout>
  <Transition name="banner">
    <div v-if="showBanner" class="cookie-banner">
      <div class="cookie-inner">
        <p>We use cookies for analytics to improve your experience. <a href="/privacy">Privacy Policy</a></p>
        <div class="cookie-actions">
          <button class="cookie-btn decline" @click="declineCookies">Decline</button>
          <button class="cookie-btn accept" @click="acceptCookies">Accept</button>
        </div>
      </div>
    </div>
  </Transition>
</template>

<style scoped>
.not-found {
  text-align: center;
  padding: 6rem 1.5rem 4rem;
}

.not-found .code {
  font-size: 4rem;
  font-weight: 700;
  font-family: 'Exo', sans-serif;
  color: var(--vp-c-brand-1);
  margin: 0;
}

.not-found h1 {
  font-size: 1.5rem;
  font-weight: 600;
  color: var(--vp-c-text-1);
  margin: 0.5rem 0;
}

.not-found .desc {
  color: var(--vp-c-text-2);
  font-size: 0.95rem;
  margin: 0.5rem 0 2rem;
}

.not-found .home-link {
  display: inline-block;
  padding: 0.625rem 1.5rem;
  background: var(--vp-c-brand-2);
  color: #fff;
  border-radius: 8px;
  font-weight: 600;
  font-family: 'Exo', sans-serif;
  text-decoration: none;
  transition: all 0.2s ease;
}

.not-found .home-link:hover {
  background: var(--vp-c-brand-3);
  box-shadow: 0 0 16px rgba(139, 92, 246, 0.4);
}

.cookie-banner {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 100;
  padding: 1rem;
  pointer-events: none;
}

.cookie-inner {
  max-width: 480px;
  margin: 0 auto 0 1rem;
  background: #111111;
  border: 1px solid #2a2a2a;
  border-radius: 12px;
  padding: 1.25rem 1.5rem;
  display: flex;
  align-items: center;
  gap: 1.25rem;
  pointer-events: auto;
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.4);
}

.cookie-inner p {
  margin: 0;
  font-size: 0.85rem;
  color: #a0a0a0;
  line-height: 1.5;
}

.cookie-inner a {
  color: var(--vp-c-brand-1);
  text-decoration: none;
}

.cookie-inner a:hover {
  text-decoration: underline;
}

.cookie-actions {
  display: flex;
  gap: 0.5rem;
  flex-shrink: 0;
}

.cookie-btn {
  padding: 0.5rem 1rem;
  border-radius: 6px;
  font-size: 0.8rem;
  font-weight: 600;
  font-family: 'Exo', sans-serif;
  cursor: pointer;
  transition: all 0.2s ease;
  border: none;
}

.cookie-btn.accept {
  background: var(--vp-c-brand-2);
  color: #fff;
}

.cookie-btn.accept:hover {
  background: var(--vp-c-brand-3);
  box-shadow: 0 0 16px rgba(139, 92, 246, 0.4);
}

.cookie-btn.decline {
  background: transparent;
  color: #707070;
  border: 1px solid #2a2a2a;
}

.cookie-btn.decline:hover {
  color: #a0a0a0;
  border-color: #3a3a3a;
}

/* Transition */
.banner-enter-active {
  transition: all 0.4s ease;
}
.banner-leave-active {
  transition: all 0.3s ease;
}
.banner-enter-from {
  opacity: 0;
  transform: translateY(20px);
}
.banner-leave-to {
  opacity: 0;
  transform: translateY(20px);
}

@media (max-width: 640px) {
  .cookie-inner {
    margin: 0;
    flex-direction: column;
    align-items: stretch;
    gap: 1rem;
  }

  .cookie-actions {
    justify-content: flex-end;
  }
}
</style>
