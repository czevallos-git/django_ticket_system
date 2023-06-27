from django.urls import path
from . import views
from . import auth

urlpatterns = [
    path('home/', views.home_page, name='home_page'),
    path('tickets/', views.tickets_page, name='tickets_page'),
    path('login/', auth.register_page, name='register_page'),
    path('register/', auth.login_page, name='login_page'),
    path('create_ticket/', views.create_ticket_page, name='create_ticket_page'),
    path('update_ticket/<str:pk>/', views.update_ticket_page, name='update_ticket_page'),
    path('delete_ticket/<str:pk>/', views.delete_ticket, name='delete_ticket'),
]