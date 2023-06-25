from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    USER_TYPE_CHOICES = [
        ('Empresa', 'Empresa'),
        ('Consumidor Final', 'Consumidor Final'),
        ('Admin da Ingresso Express', 'Admin da Ingresso Express'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=50, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return self.user.username
