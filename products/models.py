from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(
        max_length=50, 
        help_text="Help => Name of the product",
        unique=True
        )    

    description = models.CharField(
        max_length=250, 
        help_text="Help => Description of the product",
        unique=True
        )    

    nutritional_values = models.IntegerField(
        help_text="Help => Description of the Nutritional values"
        )        
    
    status = models.BooleanField(default=True)

    #user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__ (self):
        return '{}'.format(self.name)        

    def save(self):
        self.name = self.name.upper()
        super(Product, self).save()

    class Meta:
        verbose_name_plural = "Product"

class NutritionalValues(models.Model):    
    nutritionalvalues = models.ForeignKey(Product, on_delete=models.CASCADE)    
    
    name = models.CharField(
        max_length=50, 
        help_text="Help => Description od the nutritional value",
        )    
    
    unit = models.CharField(
        max_length=5, 
        help_text="Help => Description od the unit (kcal, gr.)",
        )        
    #user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__ (self):
        return '{}:{}'.format(self.product.name, self.name)        

    def save(self):
        self.descripcion = self.unit.upper()
        super(NutritionalValues, self).save()

    class Meta:
        verbose_name_plural = "Nutritional Values"
        unique_together = ('nutritionalvalues','name')

