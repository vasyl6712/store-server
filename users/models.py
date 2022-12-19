from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
	image = models.ImageField(upload_to='users_images', blank=True)

	class Meta:
		verbose_name = 'Пользователь'
		verbose_name_plural = 'Пользователи'
