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
from products.views import Class_Products_ListView, Class_Products_Create_Form, \
    Class_Home, Class_Works, \
    Class_Nutritional_Create_Form, Class_Nutritional_ListView, \
    Class_Product_Update_Form, Class_Product_Delete_Form, \
    Class_Nutritional_Update_Form, Class_Nutritional_Delete_Form, \
    Product_List_Filter_1   

urlpatterns = [
    #path('admin/', admin.site.urls),    
    path('', Class_Home.as_view(), name='home'),  
    path('works/', Class_Works.as_view(), name='works'),  
    #login/logout
    path('login/',auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='login.html'), name='logout'),    
    #product list without filter
    #path('products/list/', Class_Products_ListView.as_view(), name = 'product_list'),
    #product list with filter
    path('products/list/', Product_List_Filter_1.as_view(), name = 'product_list'),
    
    path('products/create/', Class_Products_Create_Form.as_view(), name = 'product_create'),
    path('products/update/<int:pk>', Class_Product_Update_Form.as_view(), name = 'product_update'),    
    path('products/delete/<int:pk>', Class_Product_Delete_Form.as_view(), name = 'product_delete'),    
    #nutritional
    path('nutritional/list/', Class_Nutritional_ListView.as_view(), name = 'nutritional_list'),
    path('nutritional/create/', Class_Nutritional_Create_Form.as_view(), name = 'nutritional_create'),    
    path('nutritional/update/<int:pk>', Class_Nutritional_Update_Form.as_view(), name = 'nutritional_update'),    
    path('nutritional/delete/<int:pk>', Class_Nutritional_Delete_Form.as_view(), name = 'nutritional_delete'),            
]
