# Sistema de Gestión de Empleados - Django

## Descripción
Sistema web desarrollado en Django para gestionar empleados con capacidad de manejar más de 20,000 registros usando DataTables.

## Características
- ✅ Gestión completa de empleados (CRUD)
- ✅ Interfaz moderna con DataTables
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
- DataTables (JavaScript)
- Bootstrap 5
- SQLite (desarrollo)
- Faker (generación de datos) 

¡Sí, por supuesto! El server-side processing con DataTables AJAX en Django es una técnica muy poderosa para manejar grandes volúmenes de datos en tablas web de manera eficiente.
¿Qué es?
Es una implementación donde:
DataTables (biblioteca JavaScript) se encarga de la interfaz de usuario de la tabla
Server-side processing significa que el procesamiento de datos (paginación, búsqueda, ordenamiento) se realiza en el servidor Django, no en el navegador
AJAX permite la comunicación asíncrona entre el frontend y el backend Django
¿Cómo funciona?
Frontend (DataTables):
Muestra una tabla con controles de paginación, búsqueda y ordenamiento
Cuando el usuario interactúa (cambia página, busca, ordena), envía una petición AJAX al servidor
Recibe solo los datos necesarios para la página actual
Backend (Django):
Recibe parámetros como: página actual, tamaño de página, término de búsqueda, columna de ordenamiento
Procesa estos parámetros usando el ORM de Django
Aplica filtros, ordenamiento y paginación a nivel de base de datos
Devuelve un JSON con los datos de la página actual + metadatos
Ventajas principales:
✅ Rendimiento: Solo se cargan los datos necesarios
✅ Escalabilidad: Funciona con millones de registros
✅ Experiencia de usuario: Carga rápida y fluida
✅ Eficiencia: Reduce transferencia de datos y uso de memoria