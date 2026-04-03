---
title: Política de Privacidad
description: "Política de privacidad de handled.sh. Tus datos permanecen privados: entornos aislados, tokens encriptados, sin entrenamiento de IA con tus conversaciones."
head:
  - - meta
    - property: og:title
      content: Política de Privacidad - handled.sh
  - - meta
    - property: og:description
      content: "Tus datos permanecen privados: entornos aislados, tokens encriptados, sin entrenamiento de IA con tus conversaciones."
  - - meta
    - property: og:url
      content: https://handled.sh/es/privacy
  - - link
    - rel: canonical
      href: https://handled.sh/es/privacy
---

# Política de Privacidad

**Última actualización:** 15 de febrero de 2026

handled.sh ("nosotros", "nuestro") opera el servicio de asistente personal de productividad handled.sh, disponible en [https://handled.sh](https://handled.sh). Esta política de privacidad describe qué datos recopilamos, cómo los usamos, con quién los compartimos y cómo los protegemos.

## Información que Recopilamos

### Información de Cuenta
Cuando te registras, recopilamos tu nombre, dirección de correo electrónico y foto de perfil de tu proveedor de autenticación (Google o Microsoft). Esto se utiliza para crear y administrar tu cuenta.

### Datos de Mensajería
Cuando interactúas con nuestro asistente a través de Telegram, WhatsApp o Microsoft Teams, procesamos los mensajes que envías y recibes. Esto incluye mensajes de texto, mensajes de voz, comandos y cualquier archivo o enlace que compartas con el asistente.

### Datos de Usuario de Google
Cuando conectas servicios de Google a través de nuestro panel de control, accedemos a los siguientes datos:

- **Google Calendar:** Tus eventos de calendario, incluyendo títulos de eventos, horarios, ubicaciones, descripciones y asistentes. Accedemos a estos datos para leer, crear, actualizar y eliminar eventos en tu nombre cuando le pides a tu asistente que administre tu calendario.
- **Gmail:** Accedemos a Gmail únicamente para enviar correos electrónicos en tu nombre. No leemos, escaneamos ni almacenamos el contenido de tu bandeja de entrada.

Solo solicitamos los permisos mínimos (ámbitos de OAuth) necesarios para que cada servicio funcione. Accedemos a tus datos de Google únicamente cuando le pides explícitamente a tu asistente que realice una tarea que lo requiera.

### Datos de Usuario de Microsoft
Cuando conectas servicios de Microsoft, accedemos a:

- **Microsoft Calendar:** Tus eventos de calendario, para leer y administrar tu agenda en tu nombre.
- **Outlook Mail:** Tus mensajes de correo electrónico, para leer, resumir y enviar correos en tu nombre.

### Otros Servicios Conectados
- **Todoist:** Tus tareas y proyectos, para crear, completar y administrar tareas en tu nombre.
- **WhatsApp, Telegram y Microsoft Teams:** Tus mensajes hacia y desde el asistente, para proporcionar el servicio.

### Datos de Uso
Recopilamos datos básicos de uso como marcas de tiempo de inicio de sesión, eventos de uso de funciones y registros de errores para operar y mejorar el servicio.

## Cómo Usamos tus Datos

- **Para proporcionar el servicio:** Procesar tus mensajes, ejecutar las tareas que solicitas y entregar respuestas a través de tus plataformas de mensajería conectadas.
- **Para cumplir solicitudes de integración:** Cuando le pides a tu asistente que revise tu calendario, envíe un correo electrónico o administre tareas, accedemos al servicio conectado relevante para llevar a cabo esa solicitud específica.
- **Para mejorar el servicio:** Analizar patrones de uso anonimizados y corregir problemas. No usamos tus mensajes, datos de usuario de Google o datos de servicios conectados para entrenar modelos de IA.
- **Para comunicarnos contigo:** Enviar notificaciones relacionadas con el servicio.

**No utilizamos datos de usuario de Google para mostrar publicidad, y no los usamos para ningún propósito que no sea proporcionar y mejorar el servicio handled.sh.**

## Compartir y Divulgación de Datos

### Procesamiento de IA
Tus mensajes y contexto relevante (como eventos de calendario o listas de tareas sobre las que preguntas) se envían al modelo de IA Claude de Anthropic para generar respuestas y completar tareas. Este procesamiento es estrictamente necesario para proporcionar el servicio. Anthropic no utiliza estos datos para entrenar modelos de IA. Consulta la [política de privacidad de Anthropic](https://www.anthropic.com/privacy).

### No Vendemos tus Datos
No vendemos, alquilamos, licenciamos ni intercambiamos tus datos personales o datos de usuario de Google con terceros.

### No Compartimos Datos de Usuario de Google Más Allá de lo Necesario
Los datos de usuario de Google solo se comparten con el proveedor del modelo de IA (Anthropic) en la medida necesaria para cumplir tus solicitudes específicas. Por ejemplo, si preguntas "¿Qué hay en mi calendario hoy?", tus eventos de calendario de ese día se envían al modelo de IA para generar una respuesta. No se comparten datos de usuario de Google con ningún otro tercero.

### Otras Divulgaciones
Podemos divulgar tus datos solo si así lo requiere la ley, como en respuesta a un proceso legal válido.

## Almacenamiento y Seguridad de Datos

- Todos los datos se almacenan en la infraestructura de Google Cloud Platform con encriptación en reposo.
- Todos los tokens de autenticación (Google, Microsoft, Todoist) están encriptados en reposo y almacenados por cuenta con los permisos mínimos requeridos.
- Toda la transmisión de datos utiliza encriptación HTTPS/TLS.
- El asistente de cada usuario se ejecuta en un entorno de contenedor completamente aislado. Ningún otro usuario puede acceder a tus datos, mensajes o credenciales.
- El acceso a los sistemas de producción está restringido al personal autorizado que utiliza autenticación multifactor.
- Realizamos revisiones de seguridad regulares de nuestra infraestructura y controles de acceso.

## Retención y Eliminación de Datos

- **Datos de cuenta** (nombre, correo electrónico) se retienen mientras tu cuenta esté activa.
- **Historial de conversaciones** se almacena dentro de tu contenedor aislado durante la duración de tus sesiones activas y puede borrarse periódicamente o cuando tu contenedor se reinicie.
- **Tokens de servicios conectados** (Google, Microsoft, Todoist) se retienen solo hasta que desconectes el servicio o elimines tu cuenta. Cuando desconectas un servicio desde tu panel de control, los tokens asociados se eliminan inmediatamente.
- **Datos de usuario de Google** (eventos de calendario, contenido de correo electrónico) no se almacenan permanentemente. Se obtienen en tiempo real cuando haces una solicitud, se procesan para generar una respuesta y no se retienen después de que se entrega la respuesta.
- **Datos de uso** se retienen para fines de análisis y no contienen contenido de mensajes ni datos de usuario de Google.

Puedes desconectar cualquier integración en cualquier momento desde tu [panel de control](https://handled.sh/dashboard). Puedes solicitar la eliminación completa de tu cuenta y todos los datos asociados contactándonos en [contact@handled.sh](mailto:contact@handled.sh). Procesaremos las solicitudes de eliminación dentro de 30 días.

## Tus Derechos

Tienes derecho a:

- **Acceder** a los datos personales que tenemos sobre ti.
- **Corregir** datos personales inexactos.
- **Eliminar** tu cuenta y todos los datos asociados.
- **Desconectar** cualquier servicio de terceros en cualquier momento desde tu panel de control, lo que elimina inmediatamente los tokens almacenados.
- **Exportar** tus datos bajo solicitud.
- **Revocar el acceso** a los servicios de Google en cualquier momento a través de los [permisos de tu cuenta de Google](https://myaccount.google.com/permissions).

## Privacidad de Menores

Nuestro servicio no está destinado para ser utilizado por menores de 16 años. No recopilamos datos personales de menores a sabiendas.

## Cambios a Esta Política

Podemos actualizar esta política de privacidad de vez en cuando. Si realizamos cambios en cómo usamos los datos de usuario de Google, te notificaremos por correo electrónico antes de que esos cambios entren en vigor. La fecha de "Última actualización" en la parte superior refleja la revisión más reciente.

## Contáctanos

Si tienes preguntas sobre esta política de privacidad o sobre cómo se manejan tus datos, contáctanos en:

**Correo electrónico:** [contact@handled.sh](mailto:contact@handled.sh)
