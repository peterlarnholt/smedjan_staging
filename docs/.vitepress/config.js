const sharedHead = [
  ['link', { rel: 'icon', type: 'image/svg+xml', href: '/favicon.svg' }],
  ['link', { rel: 'apple-touch-icon', href: '/favicon.svg' }],
  ['link', { rel: 'preconnect', href: 'https://fonts.googleapis.com' }],
  ['link', { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' }],
  // Open Graph
  ['meta', { property: 'og:type', content: 'website' }],
  ['meta', { property: 'og:site_name', content: 'handled.sh' }],
  ['meta', { property: 'og:image', content: 'https://handled.sh/g-hero-new-34.jpg' }],
  ['meta', { property: 'og:image:width', content: '1200' }],
  ['meta', { property: 'og:image:height', content: '630' }],

  // Twitter
  ['meta', { name: 'twitter:card', content: 'summary_large_image' }],
  ['meta', { name: 'twitter:image', content: 'https://handled.sh/g-hero-new-34.jpg' }],

  // Prevent Chrome translate bar on multilingual pages
  ['meta', { name: 'google', content: 'notranslate' }],

  // SEO
  ['meta', { name: 'keywords', content: 'productivity assistant, whatsapp bot, telegram bot, scheduling, price tracking, task management, reminder assistant, handled, google calendar, todoist, email assistant' }],
  ['meta', { name: 'author', content: 'handled.sh' }],
  ['meta', { name: 'robots', content: 'index, follow' }],

  // Google Analytics — loaded conditionally by cookie banner in Layout.vue

  // Structured Data — SoftwareApplication
  ['script', { type: 'application/ld+json' }, JSON.stringify({
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "handled.sh",
    "applicationCategory": "ProductivityApplication",
    "operatingSystem": "Web",
    "description": "Your personal productivity assistant on WhatsApp and Telegram. Manage your tasks, flights, prices, emails. Just send a message.",
    "url": "https://handled.sh",
    "offers": {
      "@type": "Offer",
      "price": "0",
      "priceCurrency": "USD"
    },
    "author": {
      "@type": "Organization",
      "name": "EXCOM AI L.L.C-FZ"
    }
  })],

  // Structured Data — Organization
  ['script', { type: 'application/ld+json' }, JSON.stringify({
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "EXCOM AI L.L.C-FZ",
    "legalName": "EXCOM AI L.L.C-FZ",
    "alternateName": "handled.sh",
    "url": "https://handled.sh",
    "logo": "https://handled.sh/logo.svg",
    "email": "contact@handled.sh",
    "contactPoint": {
      "@type": "ContactPoint",
      "email": "contact@handled.sh",
      "contactType": "Customer Support"
    }
  })],
]

const sharedNav = (texts, prefix = '', lang = '') => {
  const dashboardLink = lang
    ? `https://app.handled.sh/dashboard?lang=${lang}`
    : 'https://app.handled.sh/dashboard'
  return [
    { text: texts.home, link: `${prefix}/` },
    { text: texts.howItWorks, link: `${prefix}/how-it-works` },
    { text: texts.whoIsItFor, link: `${prefix}/use-cases` },
    { text: texts.forTeams, link: `${prefix}/teams` },
    { text: texts.pricing, link: `${prefix}/pricing` },
    { text: texts.myAssistant, link: dashboardLink, target: '_self' }
  ]
}

const sharedFooter = (texts, prefix = '', opts = {}) => ({
  message: `<a href="${prefix}/about">${texts.about}</a> · <a href="mailto:contact@handled.sh">${texts.contact}</a> · <a href="${prefix}/security">${texts.security}</a> · <a href="${prefix}/privacy">${texts.privacy}</a> · <a href="${prefix}/terms">${texts.terms}</a> · <a href="${prefix}/referral">${texts.referral}</a> · <a href="${prefix}/teams">${texts.forBusiness}</a> · <a href="${prefix}/help">${texts.help}</a> · <a href="/feedback">${texts.feedback}</a>${opts.blog ? ' · <a href="https://handled.sh/blog" onclick="window.location.href=this.href;return false;">Blog</a>' : ''}`,
  copyright: 'Copyright © 2025–2026 handled.sh — a product of EXCOM AI L.L.C-FZ'
})

export default {
  base: process.env.BASE || '/',
  vite: {
    server: {
      allowedHosts: true
    }
  },
  title: 'handled.sh - Your Personal Productivity Assistant',
  description: 'Your personal productivity assistant on WhatsApp and Telegram. Track flights, monitor prices, get summaries, manage tasks. Just send a message.',
  appearance: false,
  sitemap: {
    hostname: 'https://handled.sh'
  },
  head: sharedHead,
  locales: {
    root: {
      label: 'English',
      lang: 'en',
      themeConfig: {
        siteTitle: 'handled.sh',
        logo: { src: '/logo.svg', alt: 'handled.sh Logo' },
        nav: sharedNav({ home: 'Home', howItWorks: 'How It Works', whoIsItFor: 'Who Is It For?', forTeams: 'For Teams', pricing: 'Pricing', myAssistant: 'My Assistant' }),
        footer: sharedFooter({ about: 'About', contact: 'Contact', security: 'Security', privacy: 'Privacy Policy', terms: 'Terms of Service', referral: 'Referral Program', forBusiness: 'For Business', help: 'Help', feedback: 'Feedback' }, '', { blog: true }),
      }
    },
    es: {
      label: 'Español',
      lang: 'es',
      title: 'handled.sh - Tu Asistente de Productividad',
      description: 'Tu asistente de productividad en WhatsApp y Telegram. Gestiona tus tareas, vuelos, precios, correos. Solo envía un mensaje.',
      themeConfig: {
        siteTitle: 'handled.sh',
        logo: { src: '/logo.svg', alt: 'handled.sh Logo' },
        nav: sharedNav({ home: 'Inicio', howItWorks: 'Cómo Funciona', whoIsItFor: '¿Para Quién?', forTeams: 'Para Equipos', pricing: 'Precios', myAssistant: 'Mi Asistente' }, '/es', 'es'),
        footer: sharedFooter({ about: 'Acerca de', contact: 'Contacto', security: 'Seguridad', privacy: 'Política de Privacidad', terms: 'Términos de Servicio', referral: 'Programa de Referidos', forBusiness: 'Para Empresas', help: 'Ayuda', feedback: 'Opiniones' }, '/es'),
      }
    },
    de: {
      label: 'Deutsch',
      lang: 'de',
      title: 'handled.sh - Dein Produktivitätsassistent',
      description: 'Dein Produktivitätsassistent auf WhatsApp und Telegram. Aufgaben, Flüge, Preise, E-Mails verwalten. Einfach eine Nachricht senden.',
      themeConfig: {
        siteTitle: 'handled.sh',
        logo: { src: '/logo.svg', alt: 'handled.sh Logo' },
        nav: sharedNav({ home: 'Startseite', howItWorks: 'So Funktioniert\'s', whoIsItFor: 'Für Wen?', forTeams: 'Für Teams', pricing: 'Preise', myAssistant: 'Mein Assistent' }, '/de', 'de'),
        footer: sharedFooter({ about: 'Über uns', contact: 'Kontakt', security: 'Sicherheit', privacy: 'Datenschutz', terms: 'Nutzungsbedingungen', referral: 'Empfehlungsprogramm', forBusiness: 'Für Unternehmen', help: 'Hilfe', feedback: 'Feedback' }, '/de'),
      }
    },
    pt: {
      label: 'Português',
      lang: 'pt',
      title: 'handled.sh - Seu Assistente de Produtividade',
      description: 'Seu assistente de produtividade no WhatsApp e Telegram. Gerencie tarefas, voos, preços, e-mails. Basta enviar uma mensagem.',
      themeConfig: {
        siteTitle: 'handled.sh',
        logo: { src: '/logo.svg', alt: 'handled.sh Logo' },
        nav: sharedNav({ home: 'Início', howItWorks: 'Como Funciona', whoIsItFor: 'Para Quem?', forTeams: 'Para Equipes', pricing: 'Preços', myAssistant: 'Meu Assistente' }, '/pt', 'pt'),
        footer: sharedFooter({ about: 'Sobre', contact: 'Contato', security: 'Segurança', privacy: 'Política de Privacidade', terms: 'Termos de Serviço', referral: 'Programa de Indicação', forBusiness: 'Para Empresas', help: 'Ajuda', feedback: 'Feedback' }, '/pt'),
      }
    },
    ar: {
      label: 'العربية',
      lang: 'ar',
      dir: 'rtl',
      title: 'handled.sh - مساعد الإنتاجية الخاص بك',
      description: 'مساعد الإنتاجية الخاص بك على واتساب وتيليجرام. أدر مهامك، رحلاتك، أسعارك، بريدك. فقط أرسل رسالة.',
      themeConfig: {
        siteTitle: 'handled.sh',
        logo: { src: '/logo.svg', alt: 'handled.sh Logo' },
        nav: sharedNav({ home: 'الرئيسية', howItWorks: 'كيف يعمل', whoIsItFor: 'لمن هذا؟', forTeams: 'للفرق', pricing: 'الأسعار', myAssistant: 'مساعدي' }, '/ar', 'ar'),
        footer: sharedFooter({ about: 'عن handled', contact: 'اتصل بنا', security: 'الأمان', privacy: 'سياسة الخصوصية', terms: 'شروط الخدمة', referral: 'برنامج الإحالة', forBusiness: 'للأعمال', help: 'مساعدة', feedback: 'ملاحظات' }, '/ar'),
      }
    },
    fr: {
      label: 'Français',
      lang: 'fr',
      title: 'handled.sh - Votre Assistant de Productivité',
      description: 'Votre assistant de productivité sur WhatsApp et Telegram. Gérez vos tâches, vols, prix, e-mails. Envoyez simplement un message.',
      themeConfig: {
        siteTitle: 'handled.sh',
        logo: { src: '/logo.svg', alt: 'handled.sh Logo' },
        nav: sharedNav({ home: 'Accueil', howItWorks: 'Comment Ça Marche', whoIsItFor: 'Pour Qui ?', forTeams: 'Pour les Équipes', pricing: 'Tarifs', myAssistant: 'Mon Assistant' }, '/fr', 'fr'),
        footer: sharedFooter({ about: 'À propos', contact: 'Contact', security: 'Sécurité', privacy: 'Politique de Confidentialité', terms: 'Conditions d\'Utilisation', referral: 'Programme de Parrainage', forBusiness: 'Pour les Entreprises', help: 'Aide', feedback: 'Avis' }, '/fr'),
      }
    },
    sv: {
      label: 'Svenska',
      lang: 'sv',
      title: 'handled.sh - Din Produktivitetsassistent',
      description: 'Din produktivitetsassistent på WhatsApp och Telegram. Hantera uppgifter, flyg, priser, e-post. Skicka bara ett meddelande.',
      themeConfig: {
        siteTitle: 'handled.sh',
        logo: { src: '/logo.svg', alt: 'handled.sh Logo' },
        nav: sharedNav({ home: 'Hem', howItWorks: 'Hur Det Fungerar', whoIsItFor: 'Vem Är Det För?', forTeams: 'För Team', pricing: 'Priser', myAssistant: 'Min Assistent' }, '/sv', 'sv'),
        footer: sharedFooter({ about: 'Om oss', contact: 'Kontakt', security: 'Säkerhet', privacy: 'Integritetspolicy', terms: 'Användarvillkor', referral: 'Värvningsprogram', forBusiness: 'För Företag', help: 'Hjälp', feedback: 'Feedback' }, '/sv'),
      }
    },
  },
}
