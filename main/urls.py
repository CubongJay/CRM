from django.urls import path

from . import views
urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('customer/<int:pk>', views.get_customer, name='customer'),
    path('delete/<int:pk>', views.delete_customer, name='delete'),
    path('edit/<int:pk>', views.update_customer, name='edit'),
    path('new/', views.register_customer, name='new_customer'),


]
