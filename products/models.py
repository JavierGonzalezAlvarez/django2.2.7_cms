from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class NutritionalValues(models.Model):        
    name = models.CharField(
        max_length=50, 
        help_text="Help => Description od the nutritional value",
        )       
    
    unit = models.DecimalField(
        max_digits=20, 
        decimal_places=2,
        help_text="Help => (1.000)",
        )       

    def __str__ (self):
        return '{}'.format(self.name)       

    def save(self):
        self.name = self.name.upper()
        super(NutritionalValues, self).save()

    class Meta:
        verbose_name_plural = "Nutritional Values"
     

class Product(models.Model):
    name = models.CharField(
        max_length=50, 
        help_text="Help => Name of the product",        
        )    

    description = models.CharField(
        max_length=250, 
        help_text="Help => Description of the product",        
        )    

    nutritional_values = models.ManyToManyField(
        NutritionalValues      
        )   

    STATUS_CHOICES = (
        ('0', 'Inactive'),
        ('1', 'Active'))
    status = models.BooleanField(default=True, choices=STATUS_CHOICES)

    def __str__ (self):        
        return '{}:{}'.format(self.nutritional_values.name, self.name)               

    def save(self):
        self.name = self.name.upper()
        super(Product, self).save()

    class Meta:
        verbose_name_plural = "Product"
 
        

