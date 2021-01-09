from django.urls import path
from . import views
from .views import *
from django.contrib.auth import views as auth_views 
from django.conf import settings
from django.conf.urls.static  import static
from django.conf.urls import url
from django.views.static import serve


urlpatterns = [
    path('', views.homev, name="home"),
    path('books', views.books, name="books"),
    path('book/<int:pk>/', views.onebook, name="onebook"),
    path('login', views.loginPage, name="login"),
    path('logout', views.logoutPage, name="logout"),
    path('register', views.registerPage, name="register"),
    
    path('users', views.users, name="users"),
    path('im', views.im, name="im"),
    path('addbook', addbook, name="addbook"),
    path('janr', janr, name="janr"),
    path('delete/<str:pk_test>/', views.delete, name="delete"),
    path('update/<str:pk>/', views.updatebook, name='Update'),
    #password reset
    path('change_password/', auth_views.PasswordChangeView.as_view()),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="password_reset"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    #Download
    url(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
]