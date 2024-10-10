import django
import os
from dotenv import load_dotenv

load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_app.settings')
django.setup()

from django.contrib.auth.models import User

def create_new_user():
    user = User.objects.create_user(
        username='jane_doe', 
        password='12345',
        email='jane@example.com'
    )

    user.first_name = 'Jane'
    user.last_name = 'Doe'

    user.save()
