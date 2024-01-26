from django.db import models


class CustomUser(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    registration_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.name
