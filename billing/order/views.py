from django.shortcuts import render

def orderView(request):
	return render(request, 'order_list.html')
