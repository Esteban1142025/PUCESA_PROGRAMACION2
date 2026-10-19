# Panel Web Administrativo - Mecánica

Panel web administrativo básico para gestionar usuarios/clientes conectado directamente a Firebase Firestore usando JavaScript.

## Características

- Registro de usuarios con datos personales y de vehículo
- Lista de usuarios registrados
- Eliminación de usuarios
- Interfaz simple y responsiva
- Conexión en tiempo real con Firebase Firestore
- **Sin servidor backend** - Todo corre en el navegador

## Estructura del Proyecto

```
Proyecto mecanica/
├── index.html                    # Aplicación completa (HTML + CSS + JS)
├── FIREBASE_STRUCTURE.md         # Documentación de estructura de Firestore
└── README.md                     # Este archivo
```

## Requisitos Previos

1. **Navegador web moderno** (Chrome, Firefox, Edge, Safari)
2. **Cuenta de Firebase** (gratuita en firebase.google.com)
3. **Proyecto de Firebase** creado

## Configuración de Firebase

### 1. Crear Proyecto en Firebase

1. Ve a [Firebase Console](https://console.firebase.google.com/)
2. Crea un nuevo proyecto o selecciona uno existente
3. Habilita **Firestore Database**:
   - Ve a "Build" → "Firestore Database"
   - Crea la base de datos
   - Selecciona "Start in test mode" (para desarrollo)

### 2. Configurar Reglas de Firestore

En Firebase Console → Firestore Database → Rules, pega:

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /usuarios/{userId} {
      allow read, write: if true;
    }
  }
}
```

**Nota**: Estas reglas permiten lectura y escritura sin autenticación. Para producción, deberías agregar autenticación.

### 3. Verificar Configuración de Firebase

El archivo `index.html` ya contiene tu configuración de Firebase:

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

## Instalación y Ejecución

### Opción 1: Abrir directamente en el navegador

1. Doble clic en `index.html`
2. ¡Listo! La aplicación se abrirá en tu navegador

### Opción 2: Usar un servidor local (recomendado para desarrollo)

Si tienes Python instalado:

```bash
# Python 3
python -m http.server 8000
```

Luego abre: `http://localhost:8000`

Si tienes Node.js instalado:

```bash
npx serve
```

## Uso de la Aplicación

### Registrar un Nuevo Usuario

1. Haz clic en "Nuevo Usuario" en el menú
2. Completa los datos personales (nombre, teléfono)
3. Completa los datos del vehículo (marca, modelo, año, patente)
4. Haz clic en "Guardar Usuario"

### Ver Lista de Usuarios

- La página principal muestra todos los usuarios registrados
- Cada usuario muestra sus datos personales y del vehículo
- Puedes eliminar usuarios con el botón "Eliminar"

## Estructura de Datos en Firestore

### Colección: `usuarios`

Cada documento contiene:

```json
{
  "nombre": "Juan Pérez",
  "telefono": "+56912345678",
  "vehiculo": {
    "marca": "Toyota",
    "modelo": "Corolla",
    "anio": 2020,
    "patente": "ABC-123"
  },
  "fecha_registro": "2026-10-19T10:30:00.000Z",
  "estado": "activo"
}
```

Para más detalles, ver <ref_file file="C:\PUCESA_PROGRAMACION2\Proyecto mecanica\FIREBASE_STRUCTURE.md" />

## Troubleshooting

### Error: "Permission denied"

- Verifica que las reglas de Firestore permitan lectura y escritura
- Asegúrate de que Firestore esté habilitado en tu proyecto

### Error: "FirebaseError: No Firebase App '[DEFAULT]' has been created"

- Verifica que las credenciales en `index.html` sean correctas
- Asegúrate de que el proyecto de Firebase existe

### Los datos no se guardan

- Verifica tu conexión a internet
- Abre la consola del navegador (F12) para ver errores
- Revisa que el proyecto de Firebase sea el correcto

## Tecnologías Utilizadas

- **HTML5**: Estructura de la página
- **CSS3**: Estilos y diseño responsivo
- **JavaScript (ES6+)**: Lógica de la aplicación
- **Firebase Client SDK**: Conexión directa con Firestore desde el navegador

## Ventajas de esta Arquitectura

- **Sin servidor**: No necesitas configurar backend
- **Fácil despliegue**: Puedes hostear en GitHub Pages, Netlify, Vercel, etc.
- **Tiempo real**: Firebase se sincroniza automáticamente
- **Escalable**: Firebase maneja la infraestructura

## Despliegue

### GitHub Pages

1. Sube el archivo `index.html` a un repositorio de GitHub
2. Ve a Settings → Pages
3. Selecciona la rama main
4. ¡Listo! Tu app estará en `https://tu-usuario.github.io/tu-repo`

### Netlify

1. Arrastra la carpeta del proyecto a [Netlify Drop](https://app.netlify.com/drop)
2. ¡Listo! Obtendrás una URL instantánea

### Firebase Hosting

```bash
npm install -g firebase-tools
firebase login
firebase init hosting
firebase deploy
```

## Próximos Pasos (Futuras Mejoras)

- Autenticación de administradores
- Edición de usuarios existentes
- Búsqueda y filtrado de usuarios
- Exportación de datos a CSV/Excel
- Dashboard con estadísticas
- Historial de servicios por usuario
- Subir fotos de vehículos
- Notificaciones en tiempo real
