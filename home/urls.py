from django.urls import path, re_path
from home.views import HomeView
from .import views

app_name = 'home'

urlpatterns =[
	path('', HomeView.as_view(), name = 'home'),
	path('connect/<slug:operation>/<int:pk>/', views.change_friends, name='change_friends')
]