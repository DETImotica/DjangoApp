#URL config
from django.urls import path
from . import views

app_name = 'sensors'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('api_login/', views.api_login, name='api_login'),
    path('logout/', views.logout, name='logout'),
    path('forbidden/', views.forbidden, name='forbidden'),
    path('rooms/', views.RoomsIndexView.as_view(), name='rooms'),
    path('types/', views.TypesIndexView.as_view(), name='types'),
    path('', views.template, name='template'),
    path('rooms/<slug:room_id>/', views.RoomsIndexView.roomDetails, name="roomDetails"),
]