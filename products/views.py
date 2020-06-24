from django.views import generic
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Product, NutritionalValues
from .forms import class_Product_Form

class Class_Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'home/home.html'
    login_url = 'login'
    
class class_Products_ListView(LoginRequiredMixin, generic.ListView):
    #Esta vista debe tener unas catecteristicas a cumplir
    #Asignamos el modelo
    model = Product
    template_name = "product_list.html"
    #Importante, el contexto es la variable que le va a pasar a la vista con
    # la informacion que va a renderizar a la plantilla. A la plantilla le dijimos
    # que se va a llamar obj, por defecto Djagno le llama object, pero nosotros cambiamos 
    # el nombre con context_object_name
    context_object_name = "obj"
    #Si no estamos logeados, que nos pida logearnos
    #Si no estasmos redireccionados nos vamos a bases:html_login
    login_url = "login"

class class_Products_Create_Form(LoginRequiredMixin, generic.CreateView):
    #Esta vista debe tener unas caracteristicas a cumplir
    #Asignamos el modelo
    model = Product
    template_name = "product_create.html"
    # Importante, el contexto es la variable que le va a pasar a la vista con
    # la informacion que va a renderizar a la plantilla. A la plantilla le dijimos
    # que se va a llamar obj, por defecto Dajgno le llama object, pero nosotros cambiamos 
    # el nombre con context_object_name
    context_object_name = "obj"
    #Preguntamos que formulario va a renderizar
    form_class = class_Product_Form
    #Al dar submit que vaya a una URL. Al createView exige que se le diga
    #  a donde tiene que ir al hacer click
    #Es la ruta a donde va una vez que se crea el registro. El createView exige que se redireccione
    success_url = reverse_lazy("product_list")  
    #Si no estamos logeados, que nos pida logearnos y nos vamos a bases:html_login
    login_url = "login"
    
    #Cuando creamos el modelo habia una propiedad "crear usuario" con una foreingkey (id), no podiamos crear dos id
    #Vamos a sbreescribir la propiedad, el metodo form_valid de etsa vista para poder tener
    #  acceso a la informacion que se esta procesando o lo que se envia desde le formulario
    #  de ahí podemos coger datos de usuario que lo está procesando y manajar los datos del usuario
    def form_valid(self, form):
        #Accedemos al formulario desde este metodo                
        #Lo guarda en el formulario. Cogemos el campo "um", que es el usuario que modifica el registro
        #Coloco el user.id porque no lo puedo referencia con el foreignkey (este era para el uc), 
        #  En este caso um es un intgeger => um = models.IntegerField(null=True, blank=True)
        
        #form.instance.um = self.request.user.id
        
        #Debemos retornar si el formulario es valido. Lo ahremos sobre el Padre con super()
        #Le mandamos el formulario que hemos modificado
        return super().form_valid(form)


