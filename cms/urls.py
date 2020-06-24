"""cms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views  
from django.urls import path
from products.views import class_Products_ListView, class_Products_Create_Form, Class_Home
    

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('products/list/', class_Products_ListView.as_view(), name = 'product_list'),
    path ('products/create/', class_Products_Create_Form.as_view(), name = 'product_create'),
    path('', Class_Home.as_view(), name='home'),   
    path('login/',auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='login.html'), name='logout'),
    
]
