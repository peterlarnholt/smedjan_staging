---
title: Integritetspolicy
description: "handled.sh integritetspolicy. Din data förblir privat: isolerade miljöer, krypterade tokens, ingen AI-träning på dina konversationer."
head:
  - - meta
    - property: og:title
      content: Integritetspolicy - handled.sh
  - - meta
    - property: og:description
      content: "Din data förblir privat: isolerade miljöer, krypterade tokens, ingen AI-träning på dina konversationer."
  - - meta
    - property: og:url
      content: https://handled.sh/sv/privacy
  - - link
    - rel: canonical
      href: https://handled.sh/sv/privacy
---

# Integritetspolicy

**Senast uppdaterad:** 15 februari 2026

handled.sh ("vi", "oss", "vår") driver tjänsten handled.sh personlig produktivitetsassistent, tillgänglig på [https://handled.sh](https://handled.sh). Denna integritetspolicy beskriver vilken data vi samlar in, hur vi använder den, vem vi delar den med och hur vi skyddar den.

## Information Vi Samlar In

### Kontoinformation
När du registrerar dig samlar vi in ditt namn, e-postadress och profilbild från din autentiseringsleverantör (Google eller Microsoft). Detta används för att skapa och hantera ditt konto.

### Meddelandedata
När du interagerar med vår assistent via Telegram, WhatsApp eller Microsoft Teams behandlar vi de meddelanden du skickar och tar emot. Detta inkluderar textmeddelanden, röstmeddelanden, kommandon och eventuella filer eller länkar du delar med assistenten.

### Google-användardata
När du ansluter Google-tjänster via vår instrumentpanel får vi tillgång till följande data:

- **Google Kalender:** Dina kalenderhändelser, inklusive händelsetitlar, tider, platser, beskrivningar och deltagare. Vi får tillgång till denna data för att läsa, skapa, uppdatera och ta bort händelser å dina vägnar när du ber din assistent att hantera din kalender.
- **Gmail:** Vi får tillgång till Gmail endast för att skicka e-post å dina vägnar. Vi läser, skannar eller lagrar inte innehållet i din inkorg.

Vi begär endast de minimala behörigheter (OAuth-omfattningar) som behövs för att varje tjänst ska fungera. Vi får tillgång till din Google-data endast när du uttryckligen ber din assistent att utföra en uppgift som kräver det.

### Microsoft-användardata
När du ansluter Microsoft-tjänster får vi tillgång till:

- **Microsoft Kalender:** Dina kalenderhändelser, för att läsa och hantera ditt schema å dina vägnar.
- **Outlook Mail:** Dina e-postmeddelanden, för att läsa, sammanfatta och skicka e-post å dina vägnar.

### Andra Anslutna Tjänster
- **Todoist:** Dina uppgifter och projekt, för att skapa, slutföra och hantera uppgifter å dina vägnar.
- **WhatsApp, Telegram och Microsoft Teams:** Dina meddelanden till och från assistenten, för att tillhandahålla tjänsten.

### Användningsdata
Vi samlar in grundläggande användningsdata såsom inloggningstidsstämplar, händelser för funktionsanvändning och felloggar för att driva och förbättra tjänsten.

## Hur Vi Använder Din Data

- **För att tillhandahålla tjänsten:** Behandla dina meddelanden, utföra de uppgifter du begär och leverera svar genom dina anslutna meddelandeplattformar.
- **För att uppfylla integrationsbegäranden:** När du ber din assistent att kontrollera din kalender, skicka ett e-postmeddelande eller hantera uppgifter får vi tillgång till den relevanta anslutna tjänsten för att utföra just den begäran.
- **För att förbättra tjänsten:** Analysera anonymiserade användningsmönster och åtgärda problem. Vi använder inte dina meddelanden, Google-användardata eller data från anslutna tjänster för att träna AI-modeller.
- **För att kommunicera med dig:** Skicka tjänsterelaterade meddelanden.

**Vi använder inte Google-användardata för att visa annonser, och vi använder den inte för något annat syfte än att tillhandahålla och förbättra tjänsten handled.sh.**

## Datadelning och Utlämnande

### AI-behandling
Dina meddelanden och relevant kontext (såsom kalenderhändelser eller uppgiftslistor du frågar om) skickas till Anthropics Claude AI-modell för att generera svar och slutföra uppgifter. Denna behandling är strikt nödvändig för att tillhandahålla tjänsten. Anthropic använder inte denna data för att träna AI-modeller. Se [Anthropics integritetspolicy](https://www.anthropic.com/privacy).

### Vi Säljer Inte Din Data
Vi säljer, hyr ut, licensierar eller handlar inte med din personliga data eller Google-användardata till någon tredje part.

### Vi Delar Inte Google-användardata Utöver Vad Som Är Nödvändigt
Google-användardata delas endast med AI-modellleverantören (Anthropic) i den utsträckning som är nödvändig för att uppfylla dina specifika begäranden. Till exempel, om du frågar "Vad har jag i kalendern idag?", skickas dina kalenderhändelser för den dagen till AI-modellen för att generera ett svar. Ingen Google-användardata delas med någon annan tredje part.

### Andra Utlämnanden
Vi kan lämna ut din data endast om det krävs enligt lag, såsom som svar på en giltig rättslig process.

## Datalagring och Säkerhet

- All data lagras på Google Cloud Platform-infrastruktur med kryptering i vila.
- Alla autentiseringstokens (Google, Microsoft, Todoist) är krypterade i vila och lagras per konto med minimalt nödvändiga behörigheter.
- All dataöverföring använder HTTPS/TLS-kryptering.
- Varje användares assistent körs i en helt isolerad containermiljö. Ingen annan användare kan komma åt din data, meddelanden eller autentiseringsuppgifter.
- Tillgång till produktionssystem är begränsad till auktoriserad personal som använder multifaktorautentisering.
- Vi genomför regelbundna säkerhetsgranskningar av vår infrastruktur och åtkomstkontroller.

## Datalagring och Radering

- **Kontodata** (namn, e-post) behålls så länge ditt konto är aktivt.
- **Konversationshistorik** lagras i din isolerade container under dina aktiva sessioner och kan rensas periodiskt eller när din container startas om.
- **Tokens för anslutna tjänster** (Google, Microsoft, Todoist) behålls endast tills du kopplar bort tjänsten eller tar bort ditt konto. När du kopplar bort en tjänst från din instrumentpanel raderas de associerade tokens omedelbart.
- **Google-användardata** (kalenderhändelser, e-postinnehåll) lagras inte permanent. Den hämtas i realtid när du gör en begäran, behandlas för att generera ett svar och behålls inte efter att svaret har levererats.
- **Användningsdata** behålls för analysändamål och innehåller inte meddelandeinnehåll eller Google-användardata.

Du kan koppla bort vilken integration som helst när som helst från din [instrumentpanel](https://handled.sh/dashboard). Du kan begära fullständig radering av ditt konto och all associerad data genom att kontakta oss på [contact@handled.sh](mailto:contact@handled.sh). Vi behandlar raderingsbegäranden inom 30 dagar.

## Dina Rättigheter

Du har rätt att:

- **Få tillgång till** den personliga data vi har om dig.
- **Korrigera** felaktig personlig data.
- **Ta bort** ditt konto och all associerad data.
- **Koppla bort** vilken tredjepartstjänst som helst när som helst från din instrumentpanel, vilket omedelbart tar bort lagrade tokens.
- **Exportera** din data på begäran.
- **Återkalla åtkomst** till Google-tjänster när som helst via dina [Google-kontobehörigheter](https://myaccount.google.com/permissions).

## Barns Integritet

Vår tjänst är inte avsedd att användas av någon under 16 år. Vi samlar inte medvetet in personlig data från barn.

## Ändringar av Denna Policy

Vi kan uppdatera denna integritetspolicy då och då. Om vi gör ändringar i hur vi använder Google-användardata kommer vi att meddela dig via e-post innan dessa ändringar träder i kraft. Datumet "Senast uppdaterad" högst upp återspeglar den senaste revisionen.

## Kontakta Oss

Om du har frågor om denna integritetspolicy eller hur din data hanteras, vänligen kontakta oss på:

**E-post:** [contact@handled.sh](mailto:contact@handled.sh)
