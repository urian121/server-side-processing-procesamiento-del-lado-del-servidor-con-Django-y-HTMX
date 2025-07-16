from django.db import models


class Employee(models.Model):
    # Información personal
    first_name = models.CharField('Nombre', max_length=100)
    last_name = models.CharField('Apellido', max_length=100)
    email = models.EmailField('Email', unique=True)
    phone = models.CharField('Teléfono', max_length=20)

    # Información laboral
    employee_id = models.CharField('ID Empleado', max_length=20, unique=True)
    department = models.CharField('Departamento', max_length=100)
    position = models.CharField('Cargo', max_length=100)
    salary = models.DecimalField('Salario', max_digits=10, decimal_places=2)
    hire_date = models.DateField('Fecha de Contratación')
    is_active = models.BooleanField('Activo', default=True)

    created_at = models.DateTimeField('Creado', auto_now_add=True)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
