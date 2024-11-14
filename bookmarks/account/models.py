from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                verbose_name='User')
    date_of_birth = models.DateField(
        blank=True,
        null=True,
        verbose_name='Date of birth')
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',
                              blank=True,
                              verbose_name='Image')

    def __str__(self) -> str:
        return f'Profile of {self.user.username}'
