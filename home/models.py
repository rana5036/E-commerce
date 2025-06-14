from django.db import models # type: ignore

# Create your models here.
class Categories(models.Model):
    name=models.CharField(max_length=50)
    icon=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Product(models.Model):

    name=models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=10,decimal_places=5)
    qty=models.IntegerField()
    tax=models.FloatField()
    total=models.DecimalField(max_digits=10,decimal_places=5)
    date=models.DateTimeField(auto_now_add=True)
    net=models.DecimalField(max_digits=10,decimal_places=5,default=0.00)
    notes=models.CharField(max_length=50,default='')
    image=models.ImageField(upload_to='images/')
    Categories=models.ForeignKey(Categories,on_delete=models.CASCADE)


    def __str__(self):
        return self.name
