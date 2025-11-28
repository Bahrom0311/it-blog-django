from django.urls import path
from . import views

# O'zgaruvchi nomi aynan 'urlpatterns' bo'lishi SHART
urlpatterns = [
    path('', views.home_view, name='home'),
    path('category/<int:category_id>/', views.category_view, name='category'),
    path('post/<int:post_id>/', views.detail_view, name='detail'),
]