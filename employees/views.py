from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from django.core.paginator import Paginator
from .models import Employee

def employee_list(request):
    # Inicialmente cargamos la página sin datos
    return render(request, 'list.html')

def employee_data(request):
    """Vista HTMX para obtener datos de empleados"""
    # Parámetros de paginación y búsqueda
    page = request.GET.get('page', 1)
    per_page = request.GET.get('per_page', 25)
    search = request.GET.get('search', '')
    sort_by = request.GET.get('sort', 'id')
    sort_dir = request.GET.get('dir', 'asc')
    
    # Obtener todos los empleados
    employees = Employee.objects.all()
    
    # Aplicar búsqueda si existe
    if search:
        employees = employees.filter(
            first_name__icontains=search
        ) | employees.filter(
            last_name__icontains=search
        ) | employees.filter(
            email__icontains=search
        ) | employees.filter(
            department__icontains=search
        ) | employees.filter(
            position__icontains=search
        )
    
    # Aplicar ordenamiento
    if sort_dir == 'desc':
        sort_by = f'-{sort_by}'
    employees = employees.order_by(sort_by)
    
    # Paginación
    paginator = Paginator(employees, per_page)
    page_obj = paginator.get_page(page)
    
    # Renderizar solo la tabla para HTMX
    if request.htmx:
        html = render_to_string(
            'partials/employee_table.html',
            {'employees': page_obj, 'page_obj': page_obj}
        )
        print(f"Enviando {len(page_obj)} registros al cliente (página {page})")
        return HttpResponse(html)
    
    # Fallback para no-HTMX (poco común)
    return render(request, 'list.html', {'employees': page_obj, 'page_obj': page_obj})

def employee_count(request):
    """Vista para verificar cuántos empleados hay en total"""
    count = Employee.objects.count()
    if request.htmx:
        return HttpResponse(f"<span>{count:,}</span>")
    return JsonResponse({'total_employees': count})
