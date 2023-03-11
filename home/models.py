from django.db import models


class Feadback(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя пользователя")
    email = models.EmailField(verbose_name="Электронная почта")
    message = models.TextField(verbose_name="Сообщение")
    
    class Meta:
        db_table = "feedback"
        verbose_name = "Сообщение пользователя"
        verbose_name_plural = "Сообщения пользователей"
