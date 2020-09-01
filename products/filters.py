from .models import Product, NutritionalValues
import django_filters

class Product_List_Filter(django_filters.FilterSet):
    #name = django_filters.CharFilter(lookup_expr='icontains')
    #status = django_filters.ModelMultipleChoiceFilter(queryset=Product.objects.all())

    class Meta:
        model = Product
        #fields = ['name']
        fields = ['name', 'description', 'nutritional_values', 'status']