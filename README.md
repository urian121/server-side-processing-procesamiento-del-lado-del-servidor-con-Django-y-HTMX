# Procesamiento del lado del servidor con Django y HTMX

## Descripción
Sistema web desarrollado en Django para gestionar empleados con capacidad de manejar más de 100,000 registros utilizando HTMX para procesamiento del lado del servidor.

![Demo](https://raw.githubusercontent.com/urian121/imagenes-proyectos-github/refs/heads/master/server-side-processing-django-htmx.gif)

![Demo](https://raw.githubusercontent.com/urian121/imagenes-proyectos-github/refs/heads/master/server-side-processing-django-htmx.png)

## Características
- ✅ Gestión completa de empleados (CRUD)
- ✅ Interfaz moderna con HTMX
- ✅ Capacidad para 20,000+ registros
- ✅ Diseño ecológico con colores verde y marrón
- ✅ Generación automática de datos de prueba

## Instalación

### 1. Crear entorno virtual
```bash
python -m venv venv
venv\Scripts\activate  # En Windows
source venv/bin/activate  # En Linux/Mac
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Ejecutar migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Crear superusuario
```bash
python manage.py createsuperuser
```

### 5. Generar datos de prueba
```bash
python manage.py generate_employees 25000
```

### 6. Ejecutar servidor
```bash
python manage.py runserver
```

## Uso
- Accede a `http://127.0.0.1:8000/` para ver la lista de empleados
- Accede a `http://127.0.0.1:8000/employee/add/` para agregar nuevos empleados
- Accede a `http://127.0.0.1:8000/admin/` para el panel de administración

## Tecnologías
- Django 4.2.7
- HTMX
- Bootstrap 5
- SQLite (desarrollo)
- Faker (generación de datos) 

¡Sí, por supuesto! El procesamiento del lado del servidor con HTMX en Django es una técnica muy poderosa para manejar grandes volúmenes de datos en tablas web de manera eficiente.

### ¿Qué es?
Es una implementación donde:
- HTMX (biblioteca JavaScript) se encarga de la interfaz de usuario de la tabla
- El procesamiento del lado del servidor significa que la paginación, búsqueda y ordenamiento se realizan en el servidor Django, no en el navegador
- HTMX permite la comunicación asíncrona entre el frontend y el backend Django sin necesidad de escribir JavaScript personalizado

### ¿Cómo funciona?
**Frontend (HTMX):**
- Muestra una tabla con controles de paginación, búsqueda y ordenamiento
- Cuando el usuario interactúa (cambia página, busca, ordena), envía una petición HTMX al servidor
- Recibe fragmentos HTML con solo los datos necesarios para la página actual
**Backend (Django):**
- Recibe parámetros como: página actual, tamaño de página, término de búsqueda, columna de ordenamiento
- Procesa estos parámetros usando el ORM de Django
- Aplica filtros, ordenamiento y paginación a nivel de base de datos
- Devuelve fragmentos HTML renderizados con los datos solicitados

### Ventajas principales:
- **Rendimiento:** Solo se transfieren los datos necesarios para cada página
- **Escalabilidad:** Funciona eficientemente con miles de registros
- **Experiencia de usuario:** Interfaz fluida sin recargas completas de página
- **Simplicidad:** Menos código JavaScript que mantener
- **SEO:** El contenido se renderiza en el servidor, lo que es mejor para los motores de búsqueda
