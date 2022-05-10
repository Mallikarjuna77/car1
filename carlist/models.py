from django.db import models
class carlist(models.Model):
    CarName=models.CharField(max_length=30)
    Price=models.IntegerField()
    Ratings=models.DecimalField(max_digits=10, decimal_places=2)
    Brand=models.CharField(max_length=30)
    Modelyear=models.IntegerField()

    def __str__(self):
        return self.CarName

class Show_room(models.Model):
    Name=models.CharField(max_length=25)
    City=models.CharField(max_length=20)
    Showroom_count=models.IntegerField(default=0)

    def __str__(self):
        return self.Name

class CarModels(models.Model):
    ModelName=models.CharField(max_length=20)

    def __str__(self):
        return self.ModelName








