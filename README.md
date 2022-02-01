### Dependencias
- Celery (Worker para tareas asincronas).
- RabbitMQ (Broker de mensajeria).
- Python >= 3.2
- PostgreSQL

### ¿Cómo usar?

#### Linux:

1. Clonar Proyecto
2. Crear entorno virtual `python3 -m venv .venv`
3. entrar al entrorno vitrual `source .venv/bin/activate`
4. Instalar dependencias `pip install -r requirements.txt`
5. Crear base de datos en local
6. Ejecutar migraciones `python manage.py makemigrations` y luego `python manage.py migrate`
7. crear super ususario `python manage.py createsuperuser`
8. ingresar manualmente la base de datos dos campos en la tabla de perfiles (administrador y cliente)
9. La tabla api_user_profile agregar el usuario y su respectivo perfil que desea asignarle
10. Iniciar servidor Django `python manage.py runserver`
11. Correr Tareas periodicas de Celery desde otra consola `celery -A easymovil beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler`
12. Correr Worker de tareas Celery `celery -A easymovil worker -l INFO`
