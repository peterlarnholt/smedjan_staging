---
title: Datenschutzerklärung
description: "handled.sh Datenschutzerklärung. Ihre Daten bleiben privat: isolierte Umgebungen, verschlüsselte Tokens, kein KI-Training mit Ihren Gesprächen."
head:
  - - meta
    - property: og:title
      content: Datenschutzerklärung - handled.sh
  - - meta
    - property: og:description
      content: "Ihre Daten bleiben privat: isolierte Umgebungen, verschlüsselte Tokens, kein KI-Training mit Ihren Gesprächen."
  - - meta
    - property: og:url
      content: https://handled.sh/de/privacy
  - - link
    - rel: canonical
      href: https://handled.sh/de/privacy
---

# Datenschutzerklärung

**Zuletzt aktualisiert:** 15. Februar 2026

handled.sh („wir", „uns", „unser") betreibt den persönlichen Produktivitätsassistenten-Service handled.sh, verfügbar unter [https://handled.sh](https://handled.sh). Diese Datenschutzerklärung beschreibt, welche Daten wir sammeln, wie wir sie verwenden, mit wem wir sie teilen und wie wir sie schützen.

## Welche Informationen wir sammeln

### Kontoinformationen
Wenn Sie sich registrieren, erfassen wir Ihren Namen, Ihre E-Mail-Adresse und Ihr Profilbild von Ihrem Authentifizierungsanbieter (Google oder Microsoft). Diese Informationen werden verwendet, um Ihr Konto zu erstellen und zu verwalten.

### Nachrichtendaten
Wenn Sie mit unserem Produktivitätsassistenten über Telegram, WhatsApp oder Microsoft Teams interagieren, verarbeiten wir die Nachrichten, die Sie senden und empfangen. Dies umfasst Textnachrichten, Sprachnachrichten, Befehle sowie alle Dateien oder Links, die Sie mit dem Assistenten teilen.

### Google-Nutzerdaten
Wenn Sie Google-Dienste über unser Dashboard verbinden, greifen wir auf folgende Daten zu:

- **Google Calendar:** Ihre Kalendertermine, einschließlich Ereignistiteln, Zeiten, Orten, Beschreibungen und Teilnehmern. Wir greifen auf diese Daten zu, um Termine in Ihrem Auftrag zu lesen, zu erstellen, zu aktualisieren und zu löschen, wenn Sie Ihren Assistenten bitten, Ihren Kalender zu verwalten.
- **Gmail:** Wir greifen ausschließlich auf Gmail zu, um E-Mails in Ihrem Auftrag zu versenden. Wir lesen, scannen oder speichern nicht den Inhalt Ihres Posteingangs.

Wir fordern nur die minimal erforderlichen Berechtigungen (OAuth-Scopes) an, die für die Funktion jedes Dienstes notwendig sind. Wir greifen nur dann auf Ihre Google-Daten zu, wenn Sie Ihren Assistenten ausdrücklich bitten, eine Aufgabe auszuführen, die dies erfordert.

### Microsoft-Nutzerdaten
Wenn Sie Microsoft-Dienste verbinden, greifen wir zu auf:

- **Microsoft Calendar:** Ihre Kalendertermine, um Ihren Zeitplan in Ihrem Auftrag zu lesen und zu verwalten.
- **Outlook Mail:** Ihre E-Mail-Nachrichten, um E-Mails in Ihrem Auftrag zu lesen, zusammenzufassen und zu versenden.

### Andere verbundene Dienste
- **Todoist:** Ihre Aufgaben und Projekte, um Aufgaben in Ihrem Auftrag zu erstellen, abzuschließen und zu verwalten.
- **WhatsApp, Telegram und Microsoft Teams:** Ihre Nachrichten an und von dem Assistenten, um den Service bereitzustellen.

### Nutzungsdaten
Wir erfassen grundlegende Nutzungsdaten wie Anmeldezeitstempel, Funktionsnutzungsereignisse und Fehlerprotokolle, um den Service zu betreiben und zu verbessern.

## Wie wir Ihre Daten verwenden

- **Um den Service bereitzustellen:** Ihre Nachrichten zu verarbeiten, die von Ihnen angeforderten Aufgaben auszuführen und Antworten über Ihre verbundenen Messaging-Plattformen zu liefern.
- **Um Integrationsanfragen zu erfüllen:** Wenn Sie Ihren Assistenten bitten, Ihren Kalender zu prüfen, eine E-Mail zu senden oder Aufgaben zu verwalten, greifen wir auf den entsprechenden verbundenen Dienst zu, um diese spezifische Anfrage auszuführen.
- **Um den Service zu verbessern:** Anonymisierte Nutzungsmuster zu analysieren und Probleme zu beheben. Wir verwenden Ihre Nachrichten, Google-Nutzerdaten oder Daten verbundener Dienste nicht zum Trainieren von KI-Modellen.
- **Um mit Ihnen zu kommunizieren:** Servicebezogene Benachrichtigungen zu senden.

**Wir verwenden Google-Nutzerdaten nicht zur Schaltung von Werbung und nutzen sie nicht für andere Zwecke als die Bereitstellung und Verbesserung des handled.sh-Services.**

## Datenweitergabe und Offenlegung

### KI-Verarbeitung
Ihre Nachrichten und relevanter Kontext (wie Kalendertermine oder Aufgabenlisten, nach denen Sie fragen) werden an Anthropics Claude-KI-Modell gesendet, um Antworten zu generieren und Aufgaben zu erledigen. Diese Verarbeitung ist streng notwendig, um den Service bereitzustellen. Anthropic verwendet diese Daten nicht zum Trainieren von KI-Modellen. Siehe [Anthropics Datenschutzerklärung](https://www.anthropic.com/privacy).

### Wir verkaufen Ihre Daten nicht
Wir verkaufen, vermieten, lizenzieren oder handeln Ihre persönlichen Daten oder Google-Nutzerdaten nicht an Dritte.

### Wir geben Google-Nutzerdaten nicht über das Notwendige hinaus weiter
Google-Nutzerdaten werden nur mit dem KI-Modellanbieter (Anthropic) in dem Umfang geteilt, der zur Erfüllung Ihrer spezifischen Anfragen erforderlich ist. Wenn Sie beispielsweise fragen „Was steht heute in meinem Kalender?", werden Ihre Kalendertermine für diesen Tag an das KI-Modell gesendet, um eine Antwort zu generieren. Google-Nutzerdaten werden mit keinem anderen Dritten geteilt.

### Sonstige Offenlegungen
Wir können Ihre Daten nur dann offenlegen, wenn dies gesetzlich vorgeschrieben ist, beispielsweise als Reaktion auf einen gültigen rechtlichen Prozess.

## Datenspeicherung und Sicherheit

- Alle Daten werden auf der Google Cloud Platform-Infrastruktur mit Verschlüsselung im Ruhezustand gespeichert.
- Alle Authentifizierungs-Tokens (Google, Microsoft, Todoist) sind im Ruhezustand verschlüsselt und werden pro Konto mit den minimal erforderlichen Berechtigungen gespeichert.
- Die gesamte Datenübertragung verwendet HTTPS/TLS-Verschlüsselung.
- Der Produktivitätsassistent jedes Benutzers läuft in einer vollständig isolierten Container-Umgebung. Kein anderer Benutzer kann auf Ihre Daten, Nachrichten oder Anmeldeinformationen zugreifen.
- Der Zugriff auf Produktionssysteme ist auf autorisiertes Personal mit Multi-Faktor-Authentifizierung beschränkt.
- Wir führen regelmäßige Sicherheitsüberprüfungen unserer Infrastruktur und Zugriffskontrollen durch.

## Datenspeicherung und Löschung

- **Kontodaten** (Name, E-Mail) werden so lange aufbewahrt, wie Ihr Konto aktiv ist.
- **Gesprächsverlauf** wird in Ihrem isolierten Container für die Dauer Ihrer aktiven Sitzungen gespeichert und kann regelmäßig oder beim Neustart Ihres Containers gelöscht werden.
- **Tokens verbundener Dienste** (Google, Microsoft, Todoist) werden nur aufbewahrt, bis Sie den Dienst trennen oder Ihr Konto löschen. Wenn Sie einen Dienst von Ihrem Dashboard trennen, werden die zugehörigen Tokens sofort gelöscht.
- **Google-Nutzerdaten** (Kalendertermine, E-Mail-Inhalte) werden nicht dauerhaft gespeichert. Sie werden in Echtzeit abgerufen, wenn Sie eine Anfrage stellen, zur Generierung einer Antwort verarbeitet und nach Zustellung der Antwort nicht aufbewahrt.
- **Nutzungsdaten** werden zu Analysezwecken aufbewahrt und enthalten keine Nachrichteninhalte oder Google-Nutzerdaten.

Sie können jede Integration jederzeit von Ihrem [Dashboard](https://handled.sh/dashboard) trennen. Sie können die vollständige Löschung Ihres Kontos und aller zugehörigen Daten beantragen, indem Sie uns unter [contact@handled.sh](mailto:contact@handled.sh) kontaktieren. Wir bearbeiten Löschungsanfragen innerhalb von 30 Tagen.

## Ihre Rechte

Sie haben das Recht:

- Auf **Zugriff** auf die personenbezogenen Daten, die wir über Sie speichern.
- Ungenaue personenbezogene Daten zu **korrigieren**.
- Ihr Konto und alle zugehörigen Daten zu **löschen**.
- Jeden Drittanbieterdienst jederzeit von Ihrem Dashboard zu **trennen**, wodurch gespeicherte Tokens sofort entfernt werden.
- Ihre Daten auf Anfrage zu **exportieren**.
- Den **Zugriff widerrufen** auf Google-Dienste jederzeit über Ihre [Google-Konto-Berechtigungen](https://myaccount.google.com/permissions).

## Datenschutz für Kinder

Unser Service ist nicht für die Nutzung durch Personen unter 16 Jahren bestimmt. Wir erfassen wissentlich keine personenbezogenen Daten von Kindern.

## Änderungen dieser Richtlinie

Wir können diese Datenschutzerklärung von Zeit zu Zeit aktualisieren. Wenn wir Änderungen an der Verwendung von Google-Nutzerdaten vornehmen, werden wir Sie per E-Mail benachrichtigen, bevor diese Änderungen in Kraft treten. Das Datum „Zuletzt aktualisiert" oben gibt die letzte Überarbeitung an.

## Kontakt

Wenn Sie Fragen zu dieser Datenschutzerklärung oder zum Umgang mit Ihren Daten haben, kontaktieren Sie uns bitte unter:

**E-Mail:** [contact@handled.sh](mailto:contact@handled.sh)
