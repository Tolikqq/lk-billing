from django.db import models
from django.conf import settings
from django.utils import timezone

class Feedback(models.Model):
	text = models.CharField(verbose_name='Сообщение', max_length=5000)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	datetime = models.DateTimeField(verbose_name='Дата', default=timezone.now)
	class Meta:
		verbose_name_plural='Сообщение в техподдержку'


