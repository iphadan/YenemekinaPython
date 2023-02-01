from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class DealerProfile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    photo=models.ImageField(upload_to='DealerProfile')
    # phone = models.CharField(max_length=9,null=True,blank=True)

    def __str__(self):
        return self.user.username

#here there is one problem that i should solve 
#how can i upload morethan one photo for car class

class Car(models.Model):
    dealer =models.ForeignKey(DealerProfile,on_delete=models.DO_NOTHING)
    car_name=models.CharField(max_length=50)
    car_brand=models.CharField(max_length=55)
    car_km=models.IntegerField(default=0)
    car_condition=models.TextField()
    negotiable=models.BooleanField(default=True)
    car_color=models.CharField(max_length=55)
    car_type=models.CharField(max_length=55)
    car_price=models.FloatField(default=0.0)
    car_model=models.CharField(max_length=55)
    plate=models.CharField(max_length=55)


    def __str__(self):
        return self.dealer.user.username + self.car_model
    



