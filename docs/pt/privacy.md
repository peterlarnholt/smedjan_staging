---
title: Política de Privacidade
description: "Política de privacidade da handled.sh. Seus dados permanecem privados: ambientes isolados, tokens criptografados, sem treinamento de IA em suas conversas."
head:
  - - meta
    - property: og:title
      content: Política de Privacidade - handled.sh
  - - meta
    - property: og:description
      content: "Seus dados permanecem privados: ambientes isolados, tokens criptografados, sem treinamento de IA em suas conversas."
  - - meta
    - property: og:url
      content: https://handled.sh/pt/privacy
  - - link
    - rel: canonical
      href: https://handled.sh/pt/privacy
---

# Política de Privacidade

**Última atualização:** 15 de fevereiro de 2026

handled.sh ("nós", "nos", "nosso") opera o serviço de assistente pessoal de produtividade handled.sh, disponível em [https://handled.sh](https://handled.sh). Esta política de privacidade descreve quais dados coletamos, como os usamos, com quem os compartilhamos e como os protegemos.

## Informações que Coletamos

### Informações da Conta
Quando você se cadastra, coletamos seu nome, endereço de e-mail e foto de perfil do seu provedor de autenticação (Google ou Microsoft). Essas informações são usadas para criar e gerenciar sua conta.

### Dados de Mensagens
Quando você interage com nosso assistente via Telegram, WhatsApp ou Microsoft Teams, processamos as mensagens que você envia e recebe. Isso inclui mensagens de texto, mensagens de voz, comandos e quaisquer arquivos ou links que você compartilhe com o assistente.

### Dados de Usuário do Google
Quando você conecta serviços do Google através do nosso painel, acessamos os seguintes dados:

- **Google Calendar:** Seus eventos de calendário, incluindo títulos de eventos, horários, locais, descrições e participantes. Acessamos esses dados para ler, criar, atualizar e excluir eventos em seu nome quando você pede ao seu assistente para gerenciar seu calendário.
- **Gmail:** Acessamos o Gmail exclusivamente para enviar e-mails em seu nome. Não lemos, escaneamos ou armazenamos o conteúdo da sua caixa de entrada.

Solicitamos apenas as permissões mínimas (escopos OAuth) necessárias para que cada serviço funcione. Acessamos seus dados do Google apenas quando você pede explicitamente ao seu assistente para executar uma tarefa que os requeira.

### Dados de Usuário da Microsoft
Quando você conecta serviços da Microsoft, acessamos:

- **Microsoft Calendar:** Seus eventos de calendário, para ler e gerenciar sua agenda em seu nome.
- **Outlook Mail:** Suas mensagens de e-mail, para ler, resumir e enviar e-mails em seu nome.

### Outros Serviços Conectados
- **Todoist:** Suas tarefas e projetos, para criar, concluir e gerenciar tarefas em seu nome.
- **WhatsApp, Telegram e Microsoft Teams:** Suas mensagens de e para o assistente, para fornecer o serviço.

### Dados de Uso
Coletamos dados básicos de uso, como carimbos de data/hora de login, eventos de uso de recursos e logs de erros para operar e melhorar o serviço.

## Como Usamos Seus Dados

- **Para fornecer o serviço:** Processar suas mensagens, executar as tarefas que você solicita e entregar respostas através de suas plataformas de mensagens conectadas.
- **Para atender solicitações de integração:** Quando você pede ao seu assistente para verificar seu calendário, enviar um e-mail ou gerenciar tarefas, acessamos o serviço conectado relevante para executar essa solicitação específica.
- **Para melhorar o serviço:** Analisar padrões de uso anonimizados e corrigir problemas. Não usamos suas mensagens, dados de usuário do Google ou dados de serviços conectados para treinar modelos de IA.
- **Para comunicar com você:** Enviar notificações relacionadas ao serviço.

**Não usamos dados de usuário do Google para veicular anúncios, e não os usamos para qualquer finalidade além de fornecer e melhorar o serviço handled.sh.**

## Compartilhamento e Divulgação de Dados

### Processamento de IA
Suas mensagens e contexto relevante (como eventos de calendário ou listas de tarefas sobre os quais você pergunta) são enviados ao modelo de IA Claude da Anthropic para gerar respostas e completar tarefas. Esse processamento é estritamente necessário para fornecer o serviço. A Anthropic não usa esses dados para treinar modelos de IA. Consulte a [política de privacidade da Anthropic](https://www.anthropic.com/privacy).

### Não Vendemos Seus Dados
Não vendemos, alugamos, licenciamos ou comercializamos seus dados pessoais ou dados de usuário do Google para terceiros.

### Não Compartilhamos Dados de Usuário do Google Além do Necessário
Dados de usuário do Google são compartilhados apenas com o provedor do modelo de IA (Anthropic) na medida necessária para atender suas solicitações específicas. Por exemplo, se você pergunta "O que há na minha agenda hoje?", seus eventos de calendário daquele dia são enviados ao modelo de IA para gerar uma resposta. Nenhum dado de usuário do Google é compartilhado com qualquer outro terceiro.

### Outras Divulgações
Podemos divulgar seus dados apenas se exigido por lei, como em resposta a um processo legal válido.

## Armazenamento e Segurança de Dados

- Todos os dados são armazenados na infraestrutura do Google Cloud Platform com criptografia em repouso.
- Todos os tokens de autenticação (Google, Microsoft, Todoist) são criptografados em repouso e armazenados por conta com as permissões mínimas necessárias.
- Toda transmissão de dados usa criptografia HTTPS/TLS.
- O assistente de cada usuário é executado em um ambiente de contêiner completamente isolado. Nenhum outro usuário pode acessar seus dados, mensagens ou credenciais.
- O acesso aos sistemas de produção é restrito a pessoal autorizado usando autenticação multifator.
- Realizamos revisões regulares de segurança de nossa infraestrutura e controles de acesso.

## Retenção e Exclusão de Dados

- **Dados da conta** (nome, e-mail) são retidos enquanto sua conta estiver ativa.
- **Histórico de conversas** é armazenado dentro do seu contêiner isolado durante suas sessões ativas e pode ser limpo periodicamente ou quando seu contêiner for reiniciado.
- **Tokens de serviços conectados** (Google, Microsoft, Todoist) são retidos apenas até você desconectar o serviço ou excluir sua conta. Quando você desconecta um serviço do seu painel, os tokens associados são excluídos imediatamente.
- **Dados de usuário do Google** (eventos de calendário, conteúdo de e-mail) não são armazenados permanentemente. Eles são buscados em tempo real quando você faz uma solicitação, processados para gerar uma resposta e não são retidos após a resposta ser entregue.
- **Dados de uso** são retidos para fins de análise e não contêm conteúdo de mensagens ou dados de usuário do Google.

Você pode desconectar qualquer integração a qualquer momento no seu [painel](https://handled.sh/dashboard). Você pode solicitar a exclusão completa da sua conta e todos os dados associados entrando em contato conosco em [contact@handled.sh](mailto:contact@handled.sh). Processaremos solicitações de exclusão dentro de 30 dias.

## Seus Direitos

Você tem o direito de:

- **Acessar** os dados pessoais que mantemos sobre você.
- **Corrigir** dados pessoais imprecisos.
- **Excluir** sua conta e todos os dados associados.
- **Desconectar** qualquer serviço de terceiros a qualquer momento no seu painel, o que remove imediatamente os tokens armazenados.
- **Exportar** seus dados mediante solicitação.
- **Revogar acesso** aos serviços do Google a qualquer momento através das suas [permissões da Conta Google](https://myaccount.google.com/permissions).

## Privacidade de Crianças

Nosso serviço não se destina ao uso por menores de 16 anos. Não coletamos intencionalmente dados pessoais de crianças.

## Alterações a Esta Política

Podemos atualizar esta política de privacidade periodicamente. Se fizermos alterações em como usamos dados de usuário do Google, notificaremos você por e-mail antes que essas alterações entrem em vigor. A data de "Última atualização" no topo reflete a revisão mais recente.

## Entre em Contato

Se você tiver dúvidas sobre esta política de privacidade ou sobre como seus dados são tratados, entre em contato conosco:

**E-mail:** [contact@handled.sh](mailto:contact@handled.sh)
