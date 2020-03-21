from django.shortcuts import render
from django.views import View
from .forms import DummyForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Feedback

class FeedbackCreateView(LoginRequiredMixin, CreateView):
	model = Feedback
	fields = ['text']
	success_url = '/feedback/'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class FeedbackListView(LoginRequiredMixin, ListView):
	model = Feedback

	def get_queryset(self):
		if self.request.user.is_staff:
			return Feedback.objects.all()
		return Feedback.objects.filter(author=self.request.user)


# Писали view руками
	# def get(self, request):
	# 	#from pdb import set_trace; set_trace() отладка
	# 	form = DummyForm()
	# 	return render(request, 'form.html', {'form': form})

	# def post(self, request):
	# 	form = DummyForm(request.POST)
	# 	if form.is_valid():
	# 		context = form.cleaned_data
	# 		return render(request, 'form.html', context)
	# 	else:
	# 		return render(request, 'error.html', {'error':form.errors })
