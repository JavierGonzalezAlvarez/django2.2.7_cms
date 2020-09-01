from django.views import generic
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Product, NutritionalValues
from .forms import Class_Product_Form, Class_NutritionalValues_Form

from .filters import Product_List_Filter
from django_filters.views import FilterView


class Class_Home(LoginRequiredMixin, generic.TemplateView):
    #template_name = 'home/home.html'
    template_name = 'home/index.html'
    login_url = 'login'
    
class Class_Works(LoginRequiredMixin, generic.TemplateView):    
    template_name = 'works.html'
    login_url = 'login'

class Class_Products_ListView(LoginRequiredMixin, generic.ListView):    
    model = Product
    template_name = "product_list.html"     
    #queryset = Product.objects.order_by('name')
    context_object_name = "obj"        
    login_url = "login"
    #name=""

    #class Meta:
    #    model = Product
    #    fields = ['name', 'description']

#def filter_product(request):
        #if request.GET.get('name'):
        #filter_name = request.GET.get('name')
        #name = Product.objects.filter(name=filter_name)          
        #return render(request, "product_list.html", {'filter': name})

#def filter_product(request):
#    filter_name = Product.objects.all()
#    name = FilterSet(request.GET, queryset=filter_name)        
#    return render(request, "product_list.html", {'filter': name})
    
#def get_queryset(self):
#    queryset = super(Class_Products_ListView, self).get_queryset()    
#    filter1 = self.request.GET.get('name')                
#    if filter1 == 'CALORIES':
#        queryset = queryset.filter(name=str(filter1))                
#        #queryset = Product.objects.queryset.filter(name=str(filter1))    
#        #return Product.objects.filter(name=str(filter1))               
#    return queryset()

#def search(request):
#    product_list = Product.objects.all()
#    product_filter = Product_List_Filter(request.GET, queryset=product_list)
#    return render(request, 'product_list.html', {'filter': product_filter})

class Product_List_Filter_1(LoginRequiredMixin, FilterView):
    model = Product
    template_name = "product_list.html"  
    context_object_name = 'obj'
    filter_class = Product_List_Filter
    login_url = "login"


    #def get_queryset(request):        
    #    name = Product.objects.order_by('name')[:5]
    #    return render(request, 'product_list.html', {'name': name})
        
class Class_Products_Create_Form(LoginRequiredMixin, generic.CreateView):    
    model = Product
    template_name = "product_create.html"
    context_object_name = "obj"
    form_class = Class_Product_Form    
    success_url = reverse_lazy("product_create")      
    login_url = "login"    
    def form_valid(self, form):       
        return super().form_valid(form)

class Class_Product_Update_Form(LoginRequiredMixin, generic.UpdateView):
    model = Product
    template_name = "product_update.html"
    context_object_name = "obj"
    form_class = Class_Product_Form
    success_url = reverse_lazy("product_list")  
    login_url = "login"
    def form_valid(self, form):        
        return super().form_valid(form)

class Class_Product_Delete_Form(LoginRequiredMixin, generic.DeleteView):    
    model = Product
    template_name = "product_delete.html"    
    context_object_name = "obj"
    success_url = reverse_lazy("product_list")  
    login_url = "login"


class Class_Nutritional_Create_Form(LoginRequiredMixin, generic.CreateView):  
    model = NutritionalValues
    template_name = "nutritional_create.html"    
    context_object_name = "obj"
    form_class = Class_NutritionalValues_Form   
    success_url = reverse_lazy("nutritional_create")  
    login_url = "login"       
    def form_valid(self, form):        
        return super().form_valid(form)

class Class_Nutritional_ListView(LoginRequiredMixin, generic.ListView):   
    model = NutritionalValues
    template_name = "nutritional_list.html"   
    context_object_name = "obj"   
    login_url = "login"


class Class_Nutritional_Update_Form(LoginRequiredMixin, generic.UpdateView):
    model = NutritionalValues
    template_name = "nutritional_update.html"
    context_object_name = "obj"
    form_class = Class_NutritionalValues_Form
    success_url = reverse_lazy("nutritional_list")  
    login_url = "login"    
    def form_valid(self, form):        
        return super().form_valid(form)

class Class_Nutritional_Delete_Form(LoginRequiredMixin, generic.DeleteView):    
    model = NutritionalValues
    template_name = "nutritional_delete.html"    
    context_object_name = "obj"
    success_url = reverse_lazy("nutritional_list")  
    login_url = "login"    


