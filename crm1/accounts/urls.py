from django.urls import path
from django.contrib.auth import views as auth_views
from . import  views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/',views.registerPage,name = 'register'),
    path('login/',views.loginPage,name = 'login'),
    path('logout/',views.logoutUser,name = 'logout'),
    path('user/',views.userPage,name = 'user'),
	path('accountSetting/',views.accountSetting,name = 'accountSetting'),
    path('products/',views.products,name = 'products'),
    path('customer/<str:pk_test>/',views.customer, name ='customer'),
    path('create_form/<str:pk_test>/',views.createOrder, name = 'createOrder'),
    path('update_form/<str:pk_test>/',views.updateOrder, name = 'updateOrder'),
    path('delete_form/<str:pk_test>/',views.deleteOrder, name = 'deleteOrder'),

	path('reset_password/',auth_views.PasswordResetView.as_view(),name="reset_password"),

    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),

    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
]  

