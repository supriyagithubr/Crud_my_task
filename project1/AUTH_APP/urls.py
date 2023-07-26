from django .urls import path
from .import views



urlpatterns = [
    path('reg/', views.signUpView, name='signup_url'),
    path('lv/', views.loginView,name='loginview_url'),
    path('lov/', views.logoutView, name='lououtview_url')
]