from django.contrib.auth.models import User

User._meta.get_field('email')._unique = True
# User._meta.get_field('email')._error_messages= {'unique': ("A user with that username already exists.")}

# Create your models here.
