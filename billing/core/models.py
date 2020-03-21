from django.db import models
from django.conf import settings
from django.utils import timezone

class Balance(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	amount = models.DecimalField(verbose_name='Сумма', max_digits=18, decimal_places=2)
	datetime = models.DateTimeField(verbose_name='Дата', default=timezone.now)
	class Meta:
		verbose_name_plural='Баланс'


class Order(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	datetime = models.DateTimeField(verbose_name='Дата', default=timezone.now)
	configuration = models.ForeignKey('Configurations', on_delete=models.CASCADE)
	countuser = models.IntegerField(verbose_name='Количество пользователей')
	amount =  models.DecimalField(verbose_name='Сумма', max_digits=18, decimal_places=2)
	def __str__(self):
		return self.configuration
	class Meta:
		verbose_name = 'Заказы'
		verbose_name_plural = 'Заказы'		


class Configurations(models.Model):
	 name = models.CharField(max_length=30)
	 tarif = models.DecimalField(verbose_name='Тариф', max_digits=18, decimal_places=2)
	 def __str__(self):
	 	return self.name
	 class Meta:
	 	verbose_name_plural='Конфигурация'

