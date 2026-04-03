---
title: Politique de confidentialité
description: "Politique de confidentialité handled.sh. Vos données restent privées : environnements isolés, jetons chiffrés, aucune formation d'IA sur vos conversations."
head:
  - - meta
    - property: og:title
      content: Politique de confidentialité - handled.sh
  - - meta
    - property: og:description
      content: "Vos données restent privées : environnements isolés, jetons chiffrés, aucune formation d'IA sur vos conversations."
  - - meta
    - property: og:url
      content: https://handled.sh/fr/privacy
  - - link
    - rel: canonical
      href: https://handled.sh/fr/privacy
---

# Politique de confidentialité

**Dernière mise à jour :** 15 février 2026

handled.sh (« nous », « notre », « nos ») exploite le service d'assistant personnel de productivité handled.sh, disponible sur [https://handled.sh](https://handled.sh). Cette politique de confidentialité décrit les données que nous collectons, comment nous les utilisons, avec qui nous les partageons et comment nous les protégeons.

## Informations que nous collectons

### Informations de compte
Lorsque vous vous inscrivez, nous collectons votre nom, votre adresse e-mail et votre photo de profil depuis votre fournisseur d'authentification (Google ou Microsoft). Ces informations sont utilisées pour créer et gérer votre compte.

### Données de messagerie
Lorsque vous interagissez avec notre assistant de productivité via Telegram, WhatsApp ou Microsoft Teams, nous traitons les messages que vous envoyez et recevez. Cela inclut les messages texte, les messages vocaux, les commandes et tous les fichiers ou liens que vous partagez avec l'assistant.

### Données utilisateur Google
Lorsque vous connectez des services Google via notre tableau de bord, nous accédons aux données suivantes :

- **Google Agenda :** Vos événements d'agenda, y compris les titres d'événements, heures, lieux, descriptions et participants. Nous accédons à ces données pour lire, créer, modifier et supprimer des événements en votre nom lorsque vous demandez à votre assistant de gérer votre agenda.
- **Gmail :** Nous accédons à Gmail uniquement pour envoyer des e-mails en votre nom. Nous ne lisons, n'analysons ni ne stockons le contenu de votre boîte de réception.

Nous demandons uniquement les permissions minimales (portées OAuth) nécessaires au fonctionnement de chaque service. Nous accédons à vos données Google uniquement lorsque vous demandez explicitement à votre assistant d'effectuer une tâche qui le nécessite.

### Données utilisateur Microsoft
Lorsque vous connectez des services Microsoft, nous accédons à :

- **Calendrier Microsoft :** Vos événements d'agenda, pour lire et gérer votre emploi du temps en votre nom.
- **Outlook Mail :** Vos messages e-mail, pour lire, résumer et envoyer des e-mails en votre nom.

### Autres services connectés
- **Todoist :** Vos tâches et projets, pour créer, compléter et gérer des tâches en votre nom.
- **WhatsApp, Telegram et Microsoft Teams :** Vos messages vers et depuis l'assistant, pour fournir le service.

### Données d'utilisation
Nous collectons des données d'utilisation basiques telles que les horodatages de connexion, les événements d'utilisation des fonctionnalités et les journaux d'erreurs pour exploiter et améliorer le service.

## Comment nous utilisons vos données

- **Pour fournir le service :** Traiter vos messages, exécuter les tâches que vous demandez et délivrer des réponses via vos plateformes de messagerie connectées.
- **Pour répondre aux demandes d'intégration :** Lorsque vous demandez à votre assistant de consulter votre agenda, d'envoyer un e-mail ou de gérer des tâches, nous accédons au service connecté concerné pour effectuer cette demande spécifique.
- **Pour améliorer le service :** Analyser les modèles d'utilisation anonymisés et corriger les problèmes. Nous n'utilisons pas vos messages, vos données utilisateur Google ou les données de services connectés pour entraîner des modèles d'IA.
- **Pour communiquer avec vous :** Envoyer des notifications liées au service.

**Nous n'utilisons pas les données utilisateur Google pour diffuser des publicités, et nous ne les utilisons pour aucune autre finalité que la fourniture et l'amélioration du service handled.sh.**

## Partage et divulgation des données

### Traitement par IA
Vos messages et le contexte pertinent (tels que les événements d'agenda ou les listes de tâches sur lesquels vous posez des questions) sont envoyés au modèle d'IA Claude d'Anthropic pour générer des réponses et accomplir des tâches. Ce traitement est strictement nécessaire pour fournir le service. Anthropic n'utilise pas ces données pour entraîner des modèles d'IA. Consultez la [politique de confidentialité d'Anthropic](https://www.anthropic.com/privacy).

### Nous ne vendons pas vos données
Nous ne vendons, ne louons, ne concédons sous licence ni n'échangeons vos données personnelles ou vos données utilisateur Google avec des tiers.

### Nous ne partageons pas les données utilisateur Google au-delà du nécessaire
Les données utilisateur Google sont uniquement partagées avec le fournisseur du modèle d'IA (Anthropic) dans la mesure nécessaire pour répondre à vos demandes spécifiques. Par exemple, si vous demandez « Qu'ai-je dans mon agenda aujourd'hui ? », vos événements d'agenda pour ce jour sont envoyés au modèle d'IA pour générer une réponse. Aucune donnée utilisateur Google n'est partagée avec d'autres tiers.

### Autres divulgations
Nous pouvons divulguer vos données uniquement si requis par la loi, par exemple en réponse à une procédure juridique valide.

## Stockage et sécurité des données

- Toutes les données sont stockées sur l'infrastructure Google Cloud Platform avec chiffrement au repos.
- Tous les jetons d'authentification (Google, Microsoft, Todoist) sont chiffrés au repos et stockés par compte avec les permissions minimales requises.
- Toute transmission de données utilise le chiffrement HTTPS/TLS.
- L'assistant de productivité de chaque utilisateur fonctionne dans un environnement conteneur complètement isolé. Aucun autre utilisateur ne peut accéder à vos données, messages ou identifiants.
- L'accès aux systèmes de production est restreint au personnel autorisé utilisant l'authentification multi-facteurs.
- Nous effectuons des révisions de sécurité régulières de notre infrastructure et de nos contrôles d'accès.

## Conservation et suppression des données

- **Données de compte** (nom, e-mail) sont conservées tant que votre compte est actif.
- **Historique des conversations** est stocké dans votre conteneur isolé pendant la durée de vos sessions actives et peut être effacé périodiquement ou lorsque votre conteneur est redémarré.
- **Jetons des services connectés** (Google, Microsoft, Todoist) sont conservés uniquement jusqu'à ce que vous déconnectiez le service ou supprimiez votre compte. Lorsque vous déconnectez un service depuis votre tableau de bord, les jetons associés sont supprimés immédiatement.
- **Données utilisateur Google** (événements d'agenda, contenu des e-mails) ne sont pas stockées de manière permanente. Elles sont récupérées en temps réel lorsque vous faites une demande, traitées pour générer une réponse et non conservées après la délivrance de la réponse.
- **Données d'utilisation** sont conservées à des fins d'analyse et ne contiennent ni contenu de message ni données utilisateur Google.

Vous pouvez déconnecter toute intégration à tout moment depuis votre [tableau de bord](https://handled.sh/dashboard). Vous pouvez demander la suppression complète de votre compte et de toutes les données associées en nous contactant à [contact@handled.sh](mailto:contact@handled.sh). Nous traiterons les demandes de suppression sous 30 jours.

## Vos droits

Vous avez le droit de :

- **Accéder** aux données personnelles que nous détenons à votre sujet.
- **Corriger** les données personnelles inexactes.
- **Supprimer** votre compte et toutes les données associées.
- **Déconnecter** tout service tiers à tout moment depuis votre tableau de bord, ce qui supprime immédiatement les jetons stockés.
- **Exporter** vos données sur demande.
- **Révoquer l'accès** aux services Google à tout moment via vos [autorisations de compte Google](https://myaccount.google.com/permissions).

## Confidentialité des mineurs

Notre service n'est pas destiné à être utilisé par des personnes de moins de 16 ans. Nous ne collectons pas sciemment de données personnelles auprès d'enfants.

## Modifications de cette politique

Nous pouvons mettre à jour cette politique de confidentialité de temps à autre. Si nous apportons des modifications à la façon dont nous utilisons les données utilisateur Google, nous vous en informerons par e-mail avant que ces modifications ne prennent effet. La date « Dernière mise à jour » en haut reflète la révision la plus récente.

## Nous contacter

Si vous avez des questions sur cette politique de confidentialité ou sur la façon dont vos données sont traitées, veuillez nous contacter à :

**E-mail :** [contact@handled.sh](mailto:contact@handled.sh)
