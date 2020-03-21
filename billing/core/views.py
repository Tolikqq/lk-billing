from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Balance, Order, Configurations
from django.db.models import Sum
from django.http import HttpResponseRedirect
import datetime

class HomePageView(LoginRequiredMixin, View):
	def get(self, request):
		#from pdb import set_trace; set_trace() 
		return render(request, 'index.html')

class BalanceCreateView(LoginRequiredMixin, CreateView):
	model = Balance
	fields = ['amount']
	success_url = '/balance/'
		

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

class BalanceListView(LoginRequiredMixin, ListView):
	model = Balance

	def get_queryset(self):
		if self.request.user.is_staff:
			return Balance.objects.all()
		return Balance.objects.filter(user=self.request.user)

	def get_context_data(self,**kwargs):
		# total_prices = Balance.objects.all().aggregate(Sum('amount'))
		total_prices = Balance.objects.filter(user=self.request.user).aggregate(Sum('amount'))['amount__sum'] or 0
		context = super().get_context_data(**kwargs)
		context['balance_sum'] = total_prices
		return context


class OrderPageView(LoginRequiredMixin, ListView):
	model = Configurations
	template_name = 'order/order_form.html'
		
class OrderNewView(View):
	def get(self, request, *args, **kwargs):
		try:
			configuration = Configurations.objects.get(pk=kwargs['pk'])
		except Configurations.DoesNotExist:
			raise Http404
		return render(request, 'order/order_new.html', context={
			'configuration' : configuration
			}) 
	def post(self, request, *args, **kwargs):
		#from pdb import set_trace; set_trace() 
		if request.method == "POST":
			NewOrder = Order()
			NewOrder.configuration = Configurations.objects.get(pk=kwargs['pk'])
			NewOrder.user = request.user
			NewOrder.countuser = request.POST.get('users')
			NewOrder.amount = request.POST.get('result')
			NewOrder.datetime = datetime.datetime.now() 
			NewOrder.save()
			return HttpResponseRedirect('/orderlist/')

class OrderListView(LoginRequiredMixin, ListView):
	model = Order
	template_name = 'order/order_list.html'

	def get_queryset(self):
		if self.request.user.is_staff:
			return Order.objects.all()
		return Order.objects.filter(user=self.request.user)
