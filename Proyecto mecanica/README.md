# Sistema de Gestión de Taller Automotriz

Sistema web para gestionar clientes, vehículos y mantenimientos de un taller automotriz.

## Comenzar

1. **Configura Firebase** (si aún no lo has hecho):
   - Ve a [Firebase Console](https://console.firebase.google.com/)
   - Crea un proyecto y habilita Firestore Database
   - Habilita Authentication (Email/Password)

2. **Configura las reglas de Firestore** en Firebase Console → Firestore Database → Rules:
```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /usuarios/{userId} {
      allow read, write: if true;
    }
    match /vehiculos/{vehiculoId} {
      allow read, write: if true;
    }
    match /users_auth/{userId} {
      allow read, write: if true;
    }
    match /mantenimientos/{mantenimientoId} {
      allow read, write: if true;
    }
    match /config_visibilidad/{configId} {
      allow read, write: if true;
    }
    match /notificaciones/{notificacionId} {
      allow read, write: if true;
    }
  }
}
```

3. **Configura EmailJS** (para envío de contraseñas y notificaciones):
   - Cuenta en [EmailJS](https://www.emailjs.com/)
   - Crea un Email Service (Gmail recomendado)
   - Agrega tu Service ID en `index.html` (línea ~969)

4. **Abre el archivo** `index.html` haciendo doble clic

## Cómo usar

### Como Administrador

1. **Registrar primer usuario** (solo la primera vez):
   - Haz clic en "Regístrate aquí"
   - Ingresa email y contraseña
   - Selecciona "Administrador"

2. **Registrar clientes:**
   - Ve a "Nuevo Cliente"
   - Completa los datos del cliente
   - El sistema genera una contraseña y la envía por email

3. **Registrar vehículos:**
   - Ve a "Nuevo Vehículo"
   - Selecciona el propietario
   - Completa los datos del vehículo

4. **Registrar mantenimientos:**
   - Ve a "Nuevo Mantenimiento"
   - Selecciona el vehículo
   - Completa los datos
   - El sistema notifica al cliente automáticamente

5. **Seguimiento de estados:**
   - Ve a "Seguimiento de Estados"
   - Actualiza el estado del vehículo cuando progrese
   - Al cambiar a "listo", se notifica al cliente

6. **Configurar visibilidad de usuarios:**
   - Ve a "Configurar Visibilidad"
   - Selecciona un usuario
   - Elige qué campos puede ver (vehículos/mantenimientos)
   - El usuario solo verá esos campos cuando se loguee

### Como Usuario (Cliente)

1. **Inicia sesión** con el email y contraseña que recibiste
2. Ve a "Mis Vehículos" para ver tus vehículos
3. Ve a "Agregar Vehículo" para registrar uno nuevo
4. Solo verás los campos que el administrador configuró para ti

## Funcionalidades

- **Fase 1:** Registro de clientes con datos completos
- **Fase 2:** Registro de vehículos relacionados con clientes
- **Fase 3:** Gestión de mantenimientos con cálculo automático de costos
- **Fase 4:** Seguimiento del estado del vehículo (pendiente → entregado)
- **Fase 5:** Notificaciones automáticas al cliente (recepción, listo para entrega, pago)
- **Configuración de visibilidad:** El admin controla qué campos ve cada usuario

## Notificaciones automáticas

El sistema envía notificaciones al cliente en 3 momentos:

1. **Al registrar mantenimiento**: Notifica recepción del vehículo con número de orden
2. **Al cambiar estado a "listo"**: Notifica que el vehículo está listo para entrega
3. **Al cambiar estado a "listo" o "entregado"**: Notifica información de pago

Las notificaciones se guardan en Firestore con su estado (pendiente, enviado o fallido) para seguimiento.

## Responsive Design

El sistema funciona correctamente en móviles y tablets. Las tablas tienen scroll horizontal y los formularios están optimizados para pantallas pequeñas.

## Archivos

- `index.html` - Aplicación completa (HTML + CSS + JavaScript)
- `README.md` - Este archivo

## Troubleshooting

**Error "Missing or insufficient permissions":**
- Verifica que las reglas de Firestore incluyan todas las colecciones
- Publica las reglas en Firebase Console

**Error "auth/email-already-in-use":**
- El email ya está registrado en Firebase Authentication
- Elimínalo en Firebase Console → Authentication → Users → Delete

**No llegan los correos:**
- Verifica que EmailJS esté configurado correctamente
- Revisa el Service ID en el código
- Verifica que los templates en EmailJS tengan las variables correctas

## Para desarrolladores

Este sistema usa:
- Firebase Firestore (base de datos)
- Firebase Authentication (login)
- EmailJS (envío de correos)
- Arquitectura SPA sin backend

Compatible con Android Studio usando el mismo proyecto Firebase.
