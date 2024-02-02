from django.db import models

# Create your models here.
class ProductModel(models.Model):
    pname=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=7,decimal_places=2)
    stock=models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def is_in_stock(self):
        return self.stock>0
    
    def __str__(self) -> str:
        return self.pname
    
    class Meta:
        db_table='products'
    