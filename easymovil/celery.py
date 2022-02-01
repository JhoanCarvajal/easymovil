import os
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'easymovil.settings')

import django
django.setup()


from celery import Celery
from django.core.mail import send_mail
from easymovil import settings

from api.models import Token
from rest_framework_simplejwt.authentication import JWTAuthentication


app = Celery('easymovil')

# Using a string here means the worker doesn't have to serialize
# the configuration object to c
# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from

app.autodiscover_tasks()



@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(60.0, verifyTokensExpirated.s(), name='Every 1 seconds')



@app.task
def verifyTokensExpirated():
    subjet = "Token"
    message = "Su Token ha expirado"

    tokens = Token.objects.all()

    for token in tokens:
        try:
            jwtAuth = JWTAuthentication()
            jwtAuth.get_validated_token(token.token)
        except:
            email = token.user.email
            token.delete()
            send_mail(
                subjet, message, settings.EMAIL_HOST_USER, [email]
            )
