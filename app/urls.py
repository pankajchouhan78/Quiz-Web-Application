
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),

    path('addQuestion/', views.add_question,name='addQuestion'),
    path('register/', views.register_user,name='register'),
    path('login/', views.login_user,name='login'),
    path('logout/', views.logout_user,name='logout'),
 
]