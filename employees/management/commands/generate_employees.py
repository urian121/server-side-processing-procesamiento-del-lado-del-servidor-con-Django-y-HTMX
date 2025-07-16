from django.core.management.base import BaseCommand
from employees.models import Employee
from faker import Faker
import random
from datetime import date, timedelta

class Command(BaseCommand):
    help = 'Genera empleados de prueba'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Número de empleados a crear')

    def handle(self, *args, **options):
        fake = Faker('es_ES')
        count = options['count']
        
        departments = ['IT', 'Ventas', 'Marketing', 'Recursos Humanos', 'Contabilidad', 'Producción']
        positions = ['Analista', 'Supervisor', 'Gerente', 'Coordinador', 'Especialista', 'Asistente']
        
        self.stdout.write(f'Generando {count} empleados...')
        
        created_count = 0
        for i in range(count):
            try:
                Employee.objects.create(
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    email=fake.unique.email(),
                    phone=fake.phone_number(),
                    employee_id=f'EMP{1000 + i}',
                    department=random.choice(departments),
                    position=random.choice(positions),
                    salary=random.randint(25000, 150000),
                    hire_date=fake.date_between(start_date='-5y', end_date='today'),
                    is_active=random.choice([True, True, True, False])  # 75% activos
                )
                created_count += 1
                
                if (i + 1) % 1000 == 0:
                    self.stdout.write(f'Creados {i + 1} empleados...')
                    
            except Exception as e:
                self.stdout.write(f'Error creando empleado {i}: {e}')
        
        self.stdout.write(
            self.style.SUCCESS(f'¡Se crearon {created_count} empleados exitosamente!')
        ) 