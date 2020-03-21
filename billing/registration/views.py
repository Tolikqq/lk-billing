from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Учетная запись успешно создана для {username}')
			return redirect('index')
	else:
		form = UserRegisterForm()
	return render(request, 'registration/register.html', {'form': form})
def index(request):
	return render(request, 'core/index.html')
