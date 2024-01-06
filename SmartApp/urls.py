from django.urls import path
from SmartApp import views

urlpatterns=[
    path('Register_Page/',views.Register_Page,name="Register_Page"),
    path('Login_pg/',views.Login_pg,name="Login_pg"),
    path('Home/', views.Home, name="Home"),

    path('Registration_save/', views.Registration_save, name="Registration_save"),
    path('Login_fun/', views.Login_fun, name="Login_fun"),
    path('Logout_fn/', views.Logout_fn, name="Logout_fn"),

    path('gas_forecasting/',views.gas_forecasting,name="gas_forecasting"),
    path('Electricity_forecasting/',views.Electricity_forecasting,name="Electricity_forecasting"),

    path('Water_forecasting/',views.Water_forecasting,name="Water_forecasting"),
]