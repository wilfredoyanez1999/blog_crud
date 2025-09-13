# Blog CRUD

Este proyecto es una aplicación web de blog con funcionalidades CRUD (Crear, Leer, Actualizar, Eliminar) desarrollada con Django.

## Estructura del proyecto
- `blog/`: Aplicación principal con modelos, vistas y administración.
- `django_base/`: Configuración base de Django (settings, urls, wsgi, asgi).
- `db.sqlite3`: Base de datos SQLite utilizada por defecto.
- `requirements.txt`: Dependencias del proyecto.
- `_blog/`: Entorno virtual Python.

## Instalación
1. Clona el repositorio:
   ```powershell
   git clone https://github.com/wilfredoyanez1999/blog_crud.git
   cd blog_crud
   ```
2. Activa el entorno virtual:
   ```powershell
   .\_blog\Scripts\Activate.ps1
   ```
3. Instala las dependencias:
   ```powershell
   pip install -r requirements.txt
   ```
4. Realiza las migraciones:
   ```powershell
   python manage.py migrate
   ```
5. Ejecuta el servidor de desarrollo:
   ```powershell
   python manage.py runserver
   ```

## Uso
Accede a `http://127.0.0.1:8000/` en tu navegador para utilizar la aplicación.

## Licencia
Este proyecto está bajo la licencia MIT.
