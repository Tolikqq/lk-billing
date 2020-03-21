from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.HomePageView.as_view(),name='index'),
    path('balance/', views.BalanceListView.as_view(), name='balance'),
    path('balance/add', views.BalanceCreateView.as_view(), name='balance/add'),
    path('order/', views.OrderPageView.as_view(), name='order'),
    path('order/add-<int:pk>', views.OrderNewView.as_view(), name='order/add'),
    path('orderlist/', views.OrderListView.as_view(), name='orderlist'),
]