# Sistema de Gestión de Empleados con Django y HTMX

## Descripción
Sistema web desarrollado en Django para gestionar empleados con capacidad de manejar más de 20,000 registros utilizando HTMX para procesamiento del lado del servidor.

## Características
- ✅ Gestión completa de empleados (CRUD)
- ✅ Interfaz moderna con HTMX
- ✅ Capacidad para 20,000+ registros
- ✅ Diseño ecológico con colores verde y marrón
- ✅ Generación automática de datos de prueba

## Instalación

1. Clonar el repositorio
2. Crear un entorno virtual: `python -m venv venv`
3. Activar el entorno virtual:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Instalar dependencias: `pip install -r requirements.txt`
5. Realizar migraciones: `python manage.py migrate`
6. Generar datos de prueba: `python manage.py generate_employees 20000`
7. Iniciar el servidor: `python manage.py runserver`

## Uso

1. Acceder a http://localhost:8000/
2. Explorar la lista de empleados con funcionalidades de:
   - Paginación
   - Búsqueda
   - Ordenamiento por columnas
   - Visualización de estadísticas

## Tecnologías Utilizadas

- Django 4.2.7
- HTMX
- Bootstrap 5
- SQLite/MySQL
- Faker (para datos de prueba)

## Procesamiento del Lado del Servidor con HTMX

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
- Devuelve fragmentos HTML renderizados con los datos solicitados

### Ventajas

- **Rendimiento:** Solo se transfieren los datos necesarios para cada página
- **Escalabilidad:** Funciona eficientemente con miles de registros
- **Experiencia de usuario:** Interfaz fluida sin recargas completas de página
- **Simplicidad:** Menos código JavaScript que mantener
- **SEO:** El contenido se renderiza en el servidor, lo que es mejor para los motores de búsqueda