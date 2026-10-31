# Sistema de Gestión de Publicaciones con Django

![Django](https://img.shields.io/badge/Django-6.1.1-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

Proyecto web desarrollado con Django para gestionar publicaciones de blog. La aplicación implementa un flujo completo de lectura, creación, edición, eliminación, autenticación de usuarios, registro y control de permisos por autor.

---

## 1. Descripción general

Este proyecto sigue el patrón arquitectónico MVT de Django:

- Model: define la estructura de los datos y la persistencia en base de datos.
- View: maneja la lógica de negocio y la interacción entre el usuario y el modelo.
- Template: renderiza la interfaz HTML y presenta la información al usuario.

La aplicación está diseñada para permitir:

- Ver el listado público de publicaciones.
- Crear nuevas entradas solo si el usuario está autenticado.
- Editar una publicación solo si el usuario es el autor.
- Eliminar una publicación solo si el usuario es el autor.
- Registrarse e iniciar sesión con el sistema de autenticación de Django.
- Centralizar el estilo visual mediante archivos estáticos.

---

## 2. Funcionalidades principales

### 2.1 Lectura pública

- El listado de publicaciones se muestra a todos los usuarios.
- Cada publicación tiene un detalle individual con su contenido completo.

### 2.2 Creación de publicaciones

- La vista de creación está protegida con `LoginRequiredMixin`.
- El autor de la publicación se asigna automáticamente al usuario autenticado.
- El formulario se valida con Django y se guarda en la base de datos.

### 2.3 Edición de publicaciones

- Solo el autor puede modificar su publicación.
- La edición se realiza mediante `UpdateView` con carga del contenido actual.
- La validación de permisos se realiza comprobando si `post.author == request.user`.

### 2.4 Eliminación segura

- La eliminación se gestiona con `DeleteView`.
- La confirmación se realiza a través de una plantilla específica.
- La acción solo está permitida al creador de la publicación.

### 2.5 Autenticación y registro

- El proyecto usa las vistas y utilidades de `django.contrib.auth`.
- Se incluye un sistema de login y logout.
- El registro de usuarios se gestiona con un formulario basado en `UserCreationForm`.

### 2.6 Permisos

- Los usuarios no autenticados solo pueden consultar contenido público.
- Los usuarios autenticados pueden crear entradas.
- Las acciones de actualización y eliminación están protegidas por validación del autor.

---

## 3. Tecnologías utilizadas

- Python 3.12+
- Django 6.1.1
- SQLite 3 (base de datos local de desarrollo)
- HTML + Django Templates
- CSS estático
- Git para control de versiones

### Dependencias principales

El proyecto usa las siguientes dependencias declaradas en [requirements.txt](requirements.txt):

```txt
asgiref==3.12.1
Django==6.1.1
sqlparse==0.6.0
tzdata==2026.4
```

---

## 4. Estructura del proyecto

```txt
blog-sep-26/
├── blog/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   ├── __init__.py
│   │   ├── 0001_initial.py
│   │   └── 0002_post_author.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── django_base/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── signup/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── static/
│   └── css/
│       └── styles.css
├── templates/
│   ├── _base.html
│   ├── create.html
│   ├── detail.html
│   ├── post_delete.html
│   ├── post_update.html
│   ├── read.html
│   └── registration/
│       ├── login.html
│       └── signup.html
├── db.sqlite3
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 5. Modelo de dominio

La entidad principal del sistema es `Post`, definida en `blog/models.py`.

Campos principales:

- `title`: título de la publicación.
- `author`: relación con el usuario autenticado (`auth.User`).
- `content`: contenido principal del post.
- `created_at`: fecha de creación.
- `updated_at`: fecha de última modificación.

También se implementa `get_absolute_url()`, que permite que Django redirija correctamente a la vista de detalle después de crear o actualizar un post.

---

## 6. Instalación y configuración

### 6.1 Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd blog-sep-26
```

### 6.2 Crear entorno virtual

En Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

En Windows PowerShell:

```powershell
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
```

### 6.3 Instalar dependencias

```bash
pip install -r requirements.txt
```

### 6.4 Ejecutar migraciones

```bash
python manage.py migrate
```

### 6.5 Crear superusuario (opcional)

```bash
python manage.py createsuperuser
```

---

## 7. Ejecución del proyecto

Inicia el servidor local:

```bash
python manage.py runserver
```

Luego accede desde el navegador a:

```txt
http://127.0.0.1:8000/
```

---

## 8. Rutas principales

El proyecto cuenta con rutas para:

- Listado de publicaciones: `/`
- Detalle del post: `/post/<pk>/`
- Creación de post: `/post/create/`
- Edición de post: `/post/<pk>/update/`
- Eliminación de post: `/post/<pk>/delete/`
- Login: `/accounts/login/`
- Logout: `/accounts/logout/`
- Registro: `/accounts/signup/`

La exactitud de estas rutas se define en los archivos `blog/urls.py` y `django_base/urls.py`.

---

## 9. Seguridad y permisos

El sistema aplica principios básicos de seguridad web:

- Uso de `LoginRequiredMixin` para restringir acceso a acciones sensibles.
- Verificación del autor antes de permitir editar o borrar un recurso.
- Uso de formularios Django con validación automática.
- Protección CSRF en operaciones de tipo `POST`.

Esto garantiza que un usuario no pueda modificar o eliminar contenido ajeno.

---

## 10. Estilos y recursos estáticos

Los archivos estáticos se encuentran en la carpeta `static/` y se centralizan en:

```txt
static/css/styles.css
```

La configuración de Django incluye:

```python
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
```

Esto permite mantener una base visual consistente en toda la aplicación.

---

## 11. Flujo de trabajo con Git

El proyecto fue desarrollado siguiendo una estrategia de ramas por funcionalidad, con commits orientados a cada etapa del sistema:

1. `feature/create`: creación de formularios y vistas.
2. `feature/css`: integración de estilos y recursos estáticos.
3. `feature/update`: actualización de publicaciones.
4. `feature/delete`: eliminación segura con confirmación.
5. `feature/login-logout`: autenticación y cierre de sesión.
6. `feature/signup`: registro de usuarios.
7. `feature/permisos`: restricciones de acceso y validación de autor.

---

## 12. Preparación para despliegue

El proyecto está preparado para adaptarse a un entorno de despliegue en PaaS como Render, Railway, Fly.io o Heroku.

### Recomendaciones para producción:

- Usar `DEBUG = False`.
- Guardar `SECRET_KEY` en variables de entorno.
- Configurar `ALLOWED_HOSTS`.
- Usar una base de datos gestionada, como PostgreSQL.
- Ejecutar un servidor WSGI de producción, por ejemplo `gunicorn`.
- Configurar archivos estáticos para producción.

Ejemplo de arranque con Gunicorn:

```bash
gunicorn django_base.wsgi:application
```

---

## 13. Conclusión

Este proyecto es una aplicación web completa de blog desarrollada con Django, con enfoque en:

- arquitectura limpia,
- separación de responsabilidades,
- seguridad básica,
- experiencia de usuario clara,
- y buenas prácticas del desarrollo web con Python.

Es un ejemplo sólido de cómo construir una aplicación CRUD con autenticación, permisos y plantillas reutilizables en Django.

---

## 14. Autor

Proyecto desarrollado por José Gabriel Rojas Dagger.

---

## 15. Licencia

Este proyecto no incluye una licencia específica en el repositorio. Si vas a compartirlo o reutilizarlo públicamente, se recomienda definir una licencia como MIT o GPL según el uso que le quieras dar.
