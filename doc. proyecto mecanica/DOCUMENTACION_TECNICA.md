# Documentación Técnica - Sistema de Gestión de Taller Automotriz

## 1. Introducción

### Propósito
Este documento proporciona la información técnica necesaria para desarrolladores que trabajen en el sistema de gestión de taller automotriz, incluyendo la creación de un aplicativo web móvil.

### Audiencia Objetivo
- Desarrolladores de software
- Ingenieros frontend
- Desarrolladores de aplicaciones móviles web (PWA)

### Stack Tecnológico
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Base de Datos:** Firebase Firestore (NoSQL)
- **Autenticación:** Firebase Authentication
- **Email:** EmailJS (envío de contraseñas)
- **Arquitectura:** Single Page Application (SPA) sin backend
- **Hosting:** Firebase Hosting / Netlify / GitHub Pages

## 2. Arquitectura del Sistema

### Arquitectura General
El sistema es una Single Page Application (SPA) que funciona completamente en el navegador sin servidor backend dedicado.

```
┌─────────────────────────────────────────┐
│         Navegador Web                   │
│  ┌───────────────────────────────────┐  │
│  │   index.html (HTML + CSS + JS)   │  │
│  └───────────────────────────────────┘  │
│           ↓                              │
│  ┌───────────────────────────────────┐  │
│  │   Firebase SDK (CDN)              │  │
│  └───────────────────────────────────┘  │
│           ↓                              │
│  ┌───────────────────────────────────┐  │
│  │   Firebase Firestore              │  │
│  │   - usuarios                     │  │
│  │   - vehiculos                    │  │
│  │   - mantenimientos               │  │
│  │   - users_auth                   │  │
│  │   - config_visibilidad           │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
```

### Flujo de Datos
1. **Cliente → Firestore:** Lectura y escritura directa mediante Firebase SDK
2. **Auth → Firestore:** Verificación de roles en colección `users_auth`
3. **Visibilidad:** Configuración cargada de `config_visibilidad` al loguearse
4. **Renderizado:** DOM manipulado dinámicamente según datos y configuración

### Componentes Principales
- **Módulo de Autenticación:** Login, registro, gestión de sesiones
- **Módulo de Clientes:** CRUD de clientes
- **Módulo de Vehículos:** CRUD de vehículos, relación con clientes
- **Módulo de Mantenimientos:** Registro y seguimiento de mantenimientos
- **Módulo de Visibilidad:** Configuración de campos visibles por usuario
- **Módulo de Estados:** Seguimiento de estado de vehículos

## 3. Estructura del Proyecto

```
Proyecto mecanica/
├── index.html                    # Aplicación completa (HTML + CSS + JS)
├── clientes.json                  # Archivo JSON de ejemplo (opcional)
├── README.md                     # Documentación para usuarios finales
└── DOCUMENTACION_TECNICA.md      # Este archivo
```

### Descripción de Archivos

**index.html**
- Contiene toda la aplicación en un solo archivo
- HTML: Estructura de la aplicación
- CSS: Estilos (incluyendo responsive design)
- JavaScript: Lógica de la aplicación
- Tamaño: ~50KB (sin datos)

**clientes.json**
- Archivo de ejemplo con datos de prueba
- Formato JSON antiguo (compatible con sistema)
- No es necesario para funcionamiento

### Dependencias Externas

**Firebase SDK (v10.7.1):**
- `firebase-app.js` - Core de Firebase
- `firebase-firestore.js` - Base de datos
- `firebase-auth.js` - Autenticación
- Cargado desde CDN: `https://www.gstatic.com/firebasejs/10.7.1/`

**EmailJS (v3):**
- Envío de correos para contraseñas
- Cargado desde CDN: `https://cdn.jsdelivr.net/npm/@emailjs/browser@3/`

### Organización del Código

**Estructura en index.html:**
1. CSS (`<style>`) - Estilos globales y responsive
2. HTML - Estructura de secciones
3. EmailJS SDK - Script tradicional
4. Firebase SDK - Module script
5. JavaScript principal - Script tradicional

## 4. Configuración de Firebase

### Proyecto Firebase
- **Nombre:** proyecto-mecanica
- **Project ID:** proyecto-mecanica
- **Auth Domain:** proyecto-mecanica.firebaseapp.com

### Credenciales
Ubicadas en `index.html` (líneas ~745-753):

```javascript
const firebaseConfig = {
  apiKey: "AIzaSyBRqkX5eaB2p515F9DlVPHv_OBiONO5niE",
  authDomain: "proyecto-mecanica.firebaseapp.com",
  projectId: "proyecto-mecanica",
  storageBucket: "proyecto-mecanica.firebasestorage.app",
  messagingSenderId: "806182861434",
  appId: "1:806182861434:web:3d5f06c1c8ca94e93119c3",
  measurementId: "G-BQ37NHDXV7"
};
```

### Colecciones en Firestore
1. **usuarios** - Clientes registrados
2. **vehiculos** - Vehículos de clientes
3. **mantenimientos** - Mantenimientos de vehículos
4. **users_auth** - Roles de autenticación
5. **config_visibilidad** - Configuración de visibilidad por usuario

### Authentication
- **Método:** Email/Password
- **Habilitado:** Sí
- **Roles:** admin, usuario

## 5. Base de Datos - Firestore

### Colección: usuarios

**Propósito:** Almacenar información de clientes

**Campos:**
```json
{
  "nombres": "string",
  "apellidos": "string",
  "identificacion": "string",
  "telefono": "string",
  "correo": "string",
  "direccion": "string",
  "medio_notificacion": "string",
  "vehiculos": "array",
  "contrasena": "string",
  "fecha_registro": "timestamp (ISO string)",
  "estado": "string"
}
```

**Ejemplo:**
```json
{
  "nombres": "Juan",
  "apellidos": "Pérez",
  "identificacion": "12345678-9",
  "telefono": "+56912345678",
  "correo": "juan@email.com",
  "direccion": "Calle 123",
  "medio_notificacion": "correo",
  "vehiculos": [],
  "contrasena": "ABC123",
  "fecha_registro": "2026-11-01T10:30:00.000Z",
  "estado": "activo"
}
```

**Relaciones:**
- Un cliente puede tener múltiples vehículos (en array `vehiculos`)
- Un vehículo puede tener múltiples mantenimientos (por `vehiculo_id`)

### Colección: vehiculos

**Propósito:** Almacenar información de vehículos

**Campos:**
```json
{
  "propietario_id": "string (UID del usuario)",
  "nombre_propietario": "string",
  "placa": "string",
  "marca": "string",
  "modelo": "string",
  "anio": "number",
  "color": "string",
  "kilometraje": "number",
  "combustible": "string",
  "vin": "string",
  "fecha_registro": "timestamp (ISO string)",
  "estado": "string"
}
```

**Ejemplo:**
```json
{
  "propietario_id": "UID_DEL_USUARIO",
  "nombre_propietario": "Juan Pérez",
  "placa": "ABC-123",
  "marca": "Toyota",
  "modelo": "Corolla",
  "anio": 2020,
  "color": "Blanco",
  "kilometraje": 50000,
  "combustible": "gasolina",
  "vin": "1HGCM82633A123456",
  "fecha_registro": "2026-11-01T10:30:00.000Z",
  "estado": "activo"
}
```

**Relaciones:**
- `propietario_id` → `usuarios` (1:N)
- Un vehículo → múltiples mantenimientos (1:N)

### Colección: mantenimientos

**Propósito:** Registrar mantenimientos de vehículos

**Campos:**
```json
{
  "codigo": "string",
  "vehiculo_id": "string",
  "marca_vehiculo": "string",
  "modelo_vehiculo": "string",
  "placa_vehiculo": "string",
  "nombre_propietario": "string",
  "fecha_ingreso": "timestamp (ISO string)",
  "tipo": "string (preventivo/correctivo)",
  "descripcion": "string",
  "diagnostico": "string",
  "tecnico": "string",
  "servicios": "string",
  "repuestos": "string",
  "costo_mano_obra": "number",
  "costo_repuestos": "number",
  "impuestos": "number",
  "valor_total": "number",
  "fecha_estimada_entrega": "string (YYYY-MM-DD)",
  "fecha_real_entrega": "string (YYYY-MM-DD)",
  "estado_vehiculo": "string"
}
```

**Ejemplo:**
```json
{
  "codigo": "ORD-20261101-1234",
  "vehiculo_id": "ID_DEL_VEHICULO",
  "marca_vehiculo": "Toyota",
  "modelo_vehiculo": "Corolla",
  "placa_vehiculo": "ABC-123",
  "nombre_propietario": "Juan Pérez",
  "fecha_ingreso": "2026-11-01T10:30:00.000Z",
  "tipo": "preventivo",
  "descripcion": "Cambio de aceite",
  "diagnostico": "Aceite cambiado correctamente",
  "tecnico": "Juan Pérez",
  "servicios": "Cambio de aceite",
  "repuestos": "Aceite 5W-30 (4L)",
  "costo_mano_obra": 50.00,
  "costo_repuestos": 30.00,
  "impuestos": 16.00,
  "valor_total": 96.00,
  "fecha_estimada_entrega": "2026-11-02",
  "fecha_real_entrega": "2026-11-02",
  "estado_vehiculo": "listo"
}
```

**Relaciones:**
- `vehiculo_id` → `vehiculos` (N:1)

### Colección: users_auth

**Propósito:** Almacenar roles de autenticación

**Campos:**
```json
{
  "email": "string",
  "rol": "string (admin/usuario)"
}
```

**Ejemplo:**
```json
{
  "email": "admin@taller.com",
  "rol": "admin"
}
```

**Relaciones:**
- `email` → Firebase Authentication (1:1)

### Colección: notificaciones

**Propósito:** Registrar y rastrear notificaciones enviadas a clientes

**Campos:**
```json
{
  "destinatario": "string (email)",
  "nombre_destinatario": "string",
  "canal_comunicacion": "string (email)",
  "evento": "string (recepcion_vehiculo | vehiculo_listo | informacion_pago)",
  "mensaje": "object",
  "fecha_generacion": "timestamp (ISO string)",
  "estado_envio": "string (pendiente | enviado | fallido)",
  "mantenimiento_id": "string",
  "tipo_notificacion": "string (recepcion | listo_entrega | pago)",
  "fecha_envio": "timestamp (ISO string)",
  "error": "string (nullable)"
}
```

**Ejemplo:**
```json
{
  "destinatario": "juan@email.com",
  "nombre_destinatario": "Juan Pérez",
  "canal_comunicacion": "email",
  "evento": "recepcion_vehiculo",
  "mensaje": {
    "nombre_cliente": "Juan Pérez",
    "placa": "ABC-123",
    "fecha_ingreso": "2026-11-03T10:30:00.000Z",
    "numero_orden": "ORD-20261103-1234"
  },
  "fecha_generacion": "2026-11-03T10:30:00.000Z",
  "estado_envio": "enviado",
  "mantenimiento_id": "ID_DEL_MANTENIMIENTO",
  "tipo_notificacion": "recepcion",
  "fecha_envio": "2026-11-03T10:31:00.000Z",
  "error": null
}
```

**Relaciones:**
- `mantenimiento_id` → `mantenimientos` (N:1)
- `destinatario` → `usuarios` (por correo)

### Colección: config_visibilidad

**Propósito:** Configurar campos visibles por usuario

**Estructura de IDs:**
- Formato: `{usuarioId}_{tipo}`
- Ejemplo: `UID_DEL_USUARIO_mis_vehiculos`

**Campos:**
```json
{
  "campos": "array de strings"
}
```

**Ejemplo:**
```json
{
  "campos": ["placa", "marca", "modelo", "anio"]
}
```

**Relaciones:**
- Document ID → `usuarios` (por UID)

### Índices Recomendados

Firestore crea índices automáticamente para consultas complejas. Índices recomendados:

1. **vehiculos**
   - `propietario_id` (para filtrar vehículos de un usuario)

2. **mantenimientos**
   - `vehiculo_id` (para filtrar mantenimientos de un vehículo)
   - `estado_vehiculo` (para seguimiento)

## 6. Reglas de Firestore

### Reglas Actuales

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

### Explicación de Cada Regla

- **usuarios:** Permite lectura y escritura sin restricciones
- **vehiculos:** Permite lectura y escritura sin restricciones
- **users_auth:** Permite lectura y escritura sin restricciones
- **mantenimientos:** Permite lectura y escritura sin restricciones
- **config_visibilidad:** Permite lectura y escritura sin restricciones

### Consideraciones de Seguridad

⚠️ **IMPORTANTE:** Las reglas actuales permiten acceso completo. Para producción, implementar:

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /usuarios/{userId} {
      allow read: if request.auth != null;
      allow write: if request.auth != null && (request.auth.uid == userId || get(/databases/$(database)/documents/users_auth/$(request.auth.uid)).data.rol == 'admin');
    }
    match /vehiculos/{vehiculoId} {
      allow read: if request.auth != null;
      allow write: if request.auth != null;
    }
    match /mantenimientos/{mantenimientoId} {
      allow read: if request.auth != null;
      allow write: if request.auth != null;
    }
    match /users_auth/{userId} {
      allow read: if request.auth != null;
      allow write: if false; // Solo admin puede crear roles
    }
    match /config_visibilidad/{configId} {
      allow read: if request.auth != null;
      allow write: if get(/databases/$(database)/documents/users_auth/$(request.auth.uid)).data.rol == 'admin';
    }
  }
}
```

## 7. Sistema de Autenticación

### Firebase Authentication

**Método:** Email/Password

**Flujo de Registro:**
1. Usuario ingresa email, contraseña y rol
2. Sistema crea usuario en Firebase Authentication
3. Sistema guarda rol en colección `users_auth`
4. Sistema genera contraseña aleatoria (6 dígitos)
5. Sistema envía contraseña por EmailJS
6. Usuario puede loguearse con email y contraseña

**Flujo de Login:**
1. Usuario ingresa email y contraseña
2. Sistema autentica con Firebase Authentication
3. Sistema obtiene rol de `users_auth`
4. Sistema carga configuración de visibilidad
5. Sistema muestra vista según rol

### Roles

**admin:**
- Acceso completo a todas las secciones
- Puede ver todos los clientes, vehículos y mantenimientos
- Puede configurar visibilidad de otros usuarios
- Ve todos los campos disponibles

**usuario:**
- Solo puede ver sus propios vehículos
- Solo puede agregar vehículos bajo su nombre
- Ve solo los campos configurados por el admin
- No tiene acceso a configuración de visibilidad

### Gestión de Sesiones

**Estado de Autenticación:**
- Detectado automáticamente al cargar la página
- Usando `onAuthStateChanged` de Firebase Auth
- Persistente entre recargas de página

**Variables Globales:**
- `currentUser` - Objeto de usuario autenticado
- `userRole` - Rol del usuario ('admin' o 'usuario')
- `visibilidadUsuario` - Configuración de campos visibles

## 8. Funcionalidades Implementadas

### Fase 1: Registro de Clientes

**Descripción:** Registro de clientes con datos personales

**Requisitos Técnicos:**
- Firebase Firestore (colección `usuarios`)
- Firebase Authentication (creación de usuario)
- EmailJS (envío de contraseña)

**Funciones JavaScript:**
- `form-usuario.addEventListener('submit')` - Procesa formulario
- `generarContrasena()` - Genera contraseña aleatoria
- `enviarContrasenaPorCorreo()` - Envía contraseña por EmailJS
- `cargarClientes()` - Carga lista de clientes

**Estructura de Datos:**
Ver sección 5 - Colección: usuarios

**Flujo de Ejecución:**
1. Admin completa formulario de cliente
2. Sistema genera contraseña aleatoria
3. Sistema crea usuario en Firebase Authentication
4. Sistema guarda datos en Firestore (usuarios)
5. Sistema guarda rol en Firestore (users_auth)
6. Sistema envía contraseña por EmailJS
7. Sistema muestra mensaje de éxito

### Fase 2: Registro de Vehículos

**Descripción:** Registro de vehículos relacionados con clientes

**Requisitos Técnicos:**
- Firebase Firestore (colección `vehiculos`)
- Relación con clientes (propietario_id)

**Funciones JavaScript:**
- `form-vehiculo.addEventListener('submit')` - Procesa formulario (admin)
- `form-agregar-vehiculo.addEventListener('submit')` - Procesa formulario (usuario)
- `cargarVehiculos()` - Carga lista de vehículos (admin)
- `cargarMisVehiculos()` - Carga vehículos del usuario
- `cargarPropietarios()` - Carga selector de propietarios

**Estructura de Datos:**
Ver sección 5 - Colección: vehiculos

**Flujo de Ejecución:**
1. Admin selecciona propietario o usuario usa su propio ID
2. Sistema completa datos del vehículo
3. Sistema guarda en Firestore (vehiculos)
4. Sistema establece relación con cliente

### Fase 3: Gestión de Mantenimiento

**Descripción:** Registro y gestión de mantenimientos de vehículos

**Requisitos Técnicos:**
- Firebase Firestore (colección `mantenimientos`)
- Cálculo automático de costos
- Generación de código único

**Funciones JavaScript:**
- `form-mantenimiento.addEventListener('submit')` - Procesa formulario
- `cargarMantenimientos()` - Carga lista de mantenimientos
- `generarCodigoOrden()` - Genera código único
- `calcularValorTotalMantenimiento()` - Calcula total automáticamente

**Estructura de Datos:**
Ver sección 5 - Colección: mantenimientos

**Flujo de Ejecución:**
1. Admin selecciona vehículo
2. Sistema completa datos del mantenimiento
3. Sistema calcula valor total automáticamente
4. Sistema genera código único
5. Sistema guarda en Firestore (mantenimientos)

### Fase 4: Seguimiento de Estados

**Descripción:** Seguimiento del estado de vehículos en taller

**Requisitos Técnicos:**
- Firebase Firestore (colección `mantenimientos`)
- Estados: pendiente, diagnostico, reparacion, repuestos, listo, entregado

**Funciones JavaScript:**
- `cargarSeguimiento()` - Carga tabla de seguimiento
- `actualizarEstado()` - Actualiza estado de vehículo

**Estructura de Datos:**
Campo `estado_vehiculo` en mantenimientos

**Flujo de Ejecución:**
1. Admin ve tabla de seguimiento
2. Admin selecciona vehículo
3. Admin selecciona nuevo estado
4. Sistema actualiza en Firestore
5. Sistema refresca tabla

### Módulo de Visibilidad por Usuario

**Descripción:** Configuración de campos visibles por usuario

**Requisitos Técnicos:**
- Firebase Firestore (colección `config_visibilidad`)
- Carga automática al loguearse
- Filtrado dinámico de vistas

**Funciones JavaScript:**
- `cargarUsuariosParaVisibilidad()` - Carga lista de usuarios
- `cargarConfiguracionVisibilidad()` - Carga configuración de un usuario
- `guardarConfiguracionVisibilidad()` - Guarda configuración
- `cargarVisibilidadUsuarioActual()` - Carga configuración al loguearse
- `filtrarCampos()` - Filtra objeto según campos visibles

**Estructura de Datos:**
Ver sección 5 - Colección: config_visibilidad

**Flujo de Ejecución:**
1. Admin selecciona usuario
2. Admin selecciona tipo de datos (vehículos/mantenimientos)
3. Admin marca campos visibles
4. Sistema guarda en Firestore (config_visibilidad)
5. Cuando usuario se loguea, sistema carga configuración
6. Sistema filtra vistas según configuración

### Fase 5: Gestión de Notificaciones

**Descripción:** Sistema automático de notificaciones para eventos obligatorios

**Requisitos Técnicos:**
- Firebase Firestore (colección `notificaciones`)
- EmailJS (envío de correos)
- Tres eventos obligatorios

**Tres Eventos Obligatorios:**

**1. Recepción del Vehículo**
- Se dispara al registrar un mantenimiento
- Notifica: Nombre del cliente, placa, fecha de ingreso y número de orden
- Función: `notificarRecepcionVehiculo()`

**2. Vehículo Listo para Entrega**
- Se dispara al cambiar estado a "listo"
- Notifica: Nombre del cliente, placa, estado final y disponibilidad para retiro
- Función: `notificarVehiculoListo()`

**3. Información de Pago**
- Se dispara al cambiar estado a "listo" o "entregado"
- Notifica: Número de orden, servicios realizados y valor total a pagar
- Función: `notificarInformacionPago()`

**Estructura JSON de Notificaciones:**

Colección: `notificaciones`

```json
{
  "destinatario": "cliente@email.com",
  "nombre_destinatario": "Juan Pérez",
  "canal_comunicacion": "email",
  "evento": "recepcion_vehiculo | vehiculo_listo | informacion_pago",
  "mensaje": {
    "nombre_cliente": "Juan Pérez",
    "placa": "ABC-123",
    "fecha_ingreso": "2026-11-03T10:30:00.000Z",
    "numero_orden": "ORD-20261103-1234"
  },
  "fecha_generacion": "2026-11-03T10:30:00.000Z",
  "estado_envio": "pendiente | enviado | fallido",
  "mantenimiento_id": "ID_DEL_MANTENIMIENTO",
  "tipo_notificacion": "recepcion | listo_entrega | pago",
  "fecha_envio": "2026-11-03T10:31:00.000Z",
  "error": null
}
```

**Estados de Notificación:**
- **pendiente:** Notificación creada pero aún no enviada
- **enviado:** Notificación enviada exitosamente
- **fallido:** Error al enviar notificación (con registro del error)

**Funciones JavaScript:**
- `crearNotificacion()` - Crea notificación en Firestore
- `verificarNotificacionDuplicada()` - Evita duplicados
- `enviarNotificacionYActualizarEstado()` - Envía email y actualiza estado
- `notificarRecepcionVehiculo()` - Evento 1
- `notificarVehiculoListo()` - Evento 2
- `notificarInformacionPago()` - Evento 3

**Mecanismo para Evitar Duplicados:**
- Verifica si ya existe una notificación para el mismo evento y mantenimiento
- Solo evita duplicados si la notificación anterior no es "fallido"
- Permite reintentar si la notificación anterior falló

**Registro de Errores:**
- Si el envío falla, actualiza estado a "fallido"
- Registra el mensaje de error en el campo `error`
- Guarda la fecha de intento de envío
- Registra el error en la consola para debugging

**Configuración de EmailJS:**
- Service ID: Configurado en código (línea ~969)
- Template ID Contraseña: `template_m4ukeep`
- Template ID Mantenimiento: `template_nz2xvcw`
- Public Key: `1lj1-VXpOPEjkfZc7`

**Flujo de Ejecución:**
1. Al registrar mantenimiento → Sistema crea notificación de recepción
2. Al cambiar estado a "listo" → Sistema crea notificaciones de listo y pago
3. Sistema verifica duplicados antes de crear notificación
4. Sistema envía email mediante EmailJS
5. Sistema actualiza estado de notificación (enviado/fallido)
6. Sistema registra errores si falla el envío

## 9. Configuración de EmailJS

### Propósito
Envío automático de contraseñas a nuevos usuarios

### Cómo Configurar

1. **Crear cuenta en EmailJS:** https://www.emailjs.com/
2. **Crear Email Service:** Conectar Gmail u otro proveedor
3. **Crear Email Template:**
   ```
   {{to_name}} Bienvenido al Sistema de Gestión de Taller Automotriz

   Tu contraseña para acceder al sistema es: {{contrasena}}

   Puedes cambiar tu contraseña después de iniciar sesión.

   Saludos,
   Sistema de Gestión de Taller
   ```
4. **Obtener credenciales:** Service ID, Template ID, Public Key
5. **Configurar en index.html:** Líneas ~789-792

### Campos de Configuración

```javascript
const EMAILJS_SERVICE_ID = 'YOUR_SERVICE_ID';
const EMAILJS_TEMPLATE_ID = 'YOUR_TEMPLATE_ID';
const EMAILJS_PUBLIC_KEY = 'YOUR_PUBLIC_KEY';
```

## 10. API y Funciones JavaScript

### Funciones Principales

**Autenticación:**
- `window.authSignIn(email, password)` - Iniciar sesión
- `window.authCreateUser(email, password)` - Crear usuario
- `window.authSignOut()` - Cerrar sesión
- `window.authStateChanged(callback)` - Detectar cambios de autenticación

**Firestore:**
- `window.firestoreAddDoc(collection, data)` - Agregar documento
- `window.firestoreGetDocs(collection)` - Obtener documentos
- `window.firestoreGetDoc(docRef)` - Obtener documento específico
- `window.firestoreSetDoc(docRef, data)` - Establecer documento
- `window.firestoreDeleteDoc(docRef)` - Eliminar documento
- `window.firestoreCollection(db, path)` - Referencia a colección
- `window.firestoreDoc(db, path)` - Referencia a documento

**Funciones de Negocio:**
- `cargarClientes()` - Cargar lista de clientes
- `cargarVehiculos()` - Cargar lista de vehículos
- `cargarMisVehiculos()` - Cargar vehículos del usuario
- `cargarMantenimientos()` - Cargar mantenimientos
- `cargarSeguimiento()` - Cargar seguimiento de estados
- `cargarConfiguracionVisibilidad()` - Cargar configuración de visibilidad
- `guardarConfiguracionVisibilidad()` - Guardar configuración de visibilidad

### Manejo de Errores

**Patrón:**
```javascript
try {
  await window.firestoreAddDoc(collection, data);
  showAlert('Éxito', 'success');
} catch (error) {
  console.error('Error:', error);
  showAlert('Error: ' + error.message, 'error');
}
```

**Errores Comunes:**
- `Missing or insufficient permissions` - Reglas de Firestore incorrectas
- `auth/email-already-in-use` - Email ya registrado
- `collection is not defined` - Función no exportada correctamente

### Exportaciones Globales

**Objetos Globales:**
- `window.firestoreDB` - Instancia de Firestore
- `window.firestoreAuth` - Instancia de Auth
- `window.currentUser` - Usuario autenticado actual
- `window.userRole` - Rol del usuario
- `window.visibilidadUsuario` - Configuración de visibilidad

## 11. Responsive Design

### Breakpoints

- **Desktop:** > 1024px
- **Tablet:** 768px - 1024px
- **Mobile:** < 768px
- **Extra Small:** < 480px

### Media Queries

**Tablet (max-width: 1024px):**
- Contenedor con padding reducido
- Navegación con botones más pequeños
- Tablas con fuente más pequeña

**Mobile (max-width: 768px):**
- Navegación: botones flex-wrap, min-height 44px
- Tablas: scroll horizontal, min-width 600px
- Formularios: inputs min-height 44px, font-size 16px
- Botones: full-width, min-height 44px
- Alertas: padding reducido

**Extra Small (max-width: 480px):**
- Títulos más pequeños
- Navegación más compacta
- Tablas con menos padding

### Consideraciones Móviles

- **Tamaño de toque:** Mínimo 44px para elementos interactivos
- **Font-size 16px:** Evita zoom al enfocar inputs en iOS
- **Scroll horizontal:** Tablas con overflow-x: auto
- **Touch scrolling:** -webkit-overflow-scrolling: touch
- **Full-width:** Botones ocupan todo el ancho en móvil

## 12. Despliegue

### Opciones de Despliegue

**1. Firebase Hosting**
- Servicio oficial de Firebase
- Soporta HTTPS
- Integración con Firestore
- Comandos:
  ```bash
  npm install -g firebase-tools
  firebase login
  firebase init
  firebase deploy
  ```

**2. Netlify**
- Drag & drop
- HTTPS automático
- Deploy continuo con Git
- Arrastrar carpeta al panel de Netlify

**3. GitHub Pages**
- Integración con repositorio
- HTTPS automático
- Push al repo gh-pages

**4. Otros:**
- Vercel
- AWS S3 + CloudFront
- Azure Static Web Apps

### Configuración para Firebase Hosting

**firebase.json:**
```json
{
  "hosting": {
    "public": ".",
    "ignore": ["firebase.json", "**/.*", "**/node_modules/**"],
    "rewrites": [
      {
        "source": "**",
        "destination": "/index.html"
      }
    ]
  }
}
```

## 13. Troubleshooting

### Errores Comunes

**1. Missing or insufficient permissions**
- **Causa:** Reglas de Firestore incorrectas
- **Solución:** Actualizar reglas para incluir colección faltante

**2. auth/email-already-in-use**
- **Causa:** Email ya registrado en Firebase Authentication
- **Solución:** Eliminar usuario en Firebase Console o usar otro email

**3. collection is not defined**
- **Causa:** Función no exportada correctamente
- **Solución:** Verificar que `window.firestoreCollection` esté definido

**4. Firebase App not initialized**
- **Causa:** Firebase no está inicializado
- **Solución:** Verificar que `esperarFirebaseInicializado()` espera correctamente

**5. No se cargan datos**
- **Causa:** Colección vacía o error de lectura
- **Solución:** Verificar consola para errores, verificar datos en Firebase Console

### Debugging

**Herramientas:**
- Chrome DevTools (F12)
- Firebase Console → Firestore Database
- Firebase Console → Authentication

**Logs importantes:**
- Console.log en funciones de carga
- Catch blocks con error.message
- Estado de Firebase Auth

## 14. Guía para Desarrolladores

### Cómo Agregar Nueva Funcionalidad

1. **Definir estructura de datos:**
   - Agregar colección a Firestore
   - Definir campos y tipos
   - Actualizar reglas de Firestore

2. **Crear sección HTML:**
   - Agregar `<div id="section-nueva-funcionalidad">`
   - Crear formulario o tabla según necesidad
   - Agregar botón de navegación

3. **Implementar JavaScript:**
   - Crear función para cargar datos
   - Crear función para guardar datos
   - Agregar event listeners
   - Manejar errores

4. **Agregar a navegación:**
   - Agregar botón en nav
   - Agregar caso en `showSection()`
   - Ocultar sección en función principal

5. **Actualizar documentación:**
   - Agregar a DOCUMENTACION_TECNICA.md
   - Actualizar README.md si es visible para usuarios

### Patrones a Seguir

**Carga de datos:**
```javascript
async function cargarDatos() {
  const loading = document.getElementById('loading');
  const container = document.getElementById('container');
  
  loading.classList.remove('hidden');
  container.classList.add('hidden');
  
  try {
    await esperarFirebaseInicializado();
    const ref = window.firestoreCollection(window.firestoreDB, 'coleccion');
    const snapshot = await window.firestoreGetDocs(ref);
    
    // Procesar datos
    snapshot.forEach(doc => {
      // ...
    });
    
    container.classList.remove('hidden');
  } catch (error) {
    console.error('Error:', error);
    showAlert('Error: ' + error.message, 'error');
  } finally {
    loading.classList.add('hidden');
  }
}
```

**Guardado de datos:**
```javascript
async function guardarDatos() {
  try {
    await esperarFirebaseInicializado();
    const ref = window.firestoreCollection(window.firestoreDB, 'coleccion');
    await window.firestoreAddDoc(ref, datos);
    showAlert('Guardado exitosamente', 'success');
  } catch (error) {
    console.error('Error:', error);
    showAlert('Error: ' + error.message, 'error');
  }
}
```

### Mejores Prácticas

1. **Esperar Firebase inicializado:** Usar `esperarFirebaseInicializado()`
2. **Manejo de errores:** Siempre usar try-catch
3. **Feedback al usuario:** Usar `showAlert()` para éxito/error
4. **Validación:** Validar datos antes de guardar
5. **Responsive:** Considerar mobile-first al crear UI
6. **Documentación:** Actualizar documentación con cada cambio

## 15. Consideraciones de Seguridad

### Reglas de Firestore en Producción

Ver sección 6 para reglas de seguridad recomendadas.

### Validación de Datos

**Frontend:**
- Validar inputs HTML5 (required, pattern, type)
- Validar en JavaScript antes de enviar
- Sanitizar inputs si es necesario

**Backend:**
- Firestore tiene validación básica
- Considerar usar Cloud Functions para validación avanzada

### Protección de Información Sensible

**No exponer:**
- API Keys de servicios externos en código cliente
- Información de Firebase Authentication
- Datos de otros usuarios

**Recomendaciones:**
- Usar variables de entorno en producción
- Implementar reglas de seguridad en Firestore
- Validar permisos en el servidor (Cloud Functions)

### Contraseñas

⚠️ **IMPORTANTE:** Las contraseñas se guardan en texto plano en Firestore. Para producción:
- Implementar cambio de contraseña
- Encriptar contraseñas en Firestore
- Usar Firebase Authentication Password Reset

## 16. Desarrollo de Aplicativo Web Móvil

### Convertir a PWA (Progressive Web App)

**1. Agregar manifest.json:**
```json
{
  "name": "Sistema de Gestión de Taller",
  "short_name": "Taller",
  "start_url": "./index.html",
  "display": "standalone",
  "background_color": "#ffffff",
  "theme_color": "#2c3e50",
  "icons": [
    {
      "src": "icon-192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "icon-512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ]
}
```

**2. Agregar Service Worker:**
```javascript
// sw.js
self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open('taller-v1').then((cache) => {
      return cache.addAll(['./index.html']);
    })
  );
});

self.addEventListener('fetch', (e) => {
  e.respondWith(
    caches.match(e.request).then((response) => {
      return response || fetch(e.request);
    })
  );
});
```

**3. Registrar Service Worker en index.html:**
```javascript
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('./sw.js');
}
```

**4. Agregar meta tags:**
```html
<meta name="theme-color" content="#2c3e50">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black">
<link rel="manifest" href="manifest.json">
```

### Consideraciones Móviles

- **Touch targets:** Mínimo 44px
- **Viewport:** Configurado correctamente
- **Network:** Considerar offline con Service Worker
- **Performance:** Optimizar carga de Firebase SDK
- **UX:** Evitar popups en móvil (usar modales en su lugar)

### Testing en Móvil

**1. Chrome DevTools Device Mode:**
- F12 → Toggle device toolbar
- Seleccionar dispositivo
- Probar responsive

**2. Dispositivo Real:**
- Desplegar a Firebase Hosting
- Abrir URL en móvil
- Probar todas las funcionalidades

**3. iOS vs Android:**
- iOS: Safari tiene comportamiento diferente con zoom
- Android: Chrome es el navegador principal
- Probar en ambos

## 17. Estructura de Código para Aplicativo Web

### Recomendación: Separar Archivos

Para desarrollo de aplicativo web, separar en archivos:

```
app/
├── index.html
├── css/
│   ├── styles.css
│   └── responsive.css
├── js/
│   ├── firebase-config.js
│   ├── auth.js
│   ├── clientes.js
│   ├── vehiculos.js
│   ├── mantenimientos.js
│   └── main.js
├── assets/
│   ├── icons/
│   └── images/
├── manifest.json
└── sw.js
```

### Firebase Config Separado

**firebase-config.js:**
```javascript
const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "your-project.firebaseapp.com",
  projectId: "your-project",
  // ...
};

export default firebaseConfig;
```

### Módulos JavaScript

Usar ES6 modules para mejor organización:

```javascript
// auth.js
export function login(email, password) { }
export function register(email, password) { }
export function logout() { }

// main.js
import { login, register, logout } from './auth.js';
```

## 18. Conclusiones

Este sistema es una SPA completa sin backend que utiliza Firebase para todas las operaciones de base de datos y autenticación. La arquitectura es simple pero escalable, ideal para pequeños y medianos talleres automotrices.

**Recursos:**
- Firebase Documentation: https://firebase.google.com/docs
- Firestore Rules: https://firebase.google.com/docs/firestore/security/rules
- PWA Guide: https://web.dev/progressive-web-apps/
