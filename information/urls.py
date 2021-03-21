from django.urls import path 
from . import views

app_name= 'infor'
urlpatterns = [
    path('',views.index,name='index'),
    path ('<int:infor_id>',views.detail,name='detail'),
    path('login/',views.login_page,name='login'),
    path('logout/',views.logout_User,name='logout'),
    path('registration/',views.registration_page,name='registration')
]