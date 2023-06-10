from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Bus_details(models.Model):
    admin_id = models.IntegerField()
    bus_type = models.CharField(max_length=100)
    travels_name=models.CharField(max_length=100)
    start_location = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    nos = models.DecimalField(decimal_places=0, max_digits=2,default=35)
    rem = models.DecimalField(decimal_places=0, max_digits=2,default=35)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.TimeField()
    bus_status=models.CharField(max_length=20,default="Yet to start")

    def __str__(self):
        return f"{self.start_location} - {self.destination}"

class User_Details(models.Model):
    #user_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    mailid=models.CharField(max_length=50)
    last_login = models.DateTimeField(auto_now=True)
    password=models.CharField(max_length=20)
    repassword=models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'

class Book(models.Model):
    booked='B'
    cancelled='C'
    ticket_status=((booked,'Booked'),(cancelled,'Cancelled'))
    user_id = models.DecimalField(decimal_places=0, max_digits=2)
    bus_id=models.DecimalField(decimal_places=0,max_digits=2)
    name=models.CharField(max_length=50)
    mailid=models.EmailField()
    bus_type=models.CharField(max_length=50)
    source=models.CharField(max_length=50)
    dest = models.CharField(max_length=50)
    pass_name=models.CharField(max_length=50)
    pass_gender=models.CharField(max_length=10)
    travels_name=models.CharField(max_length=100)
    pass_age=models.IntegerField()
    price=models.DecimalField(decimal_places=2,max_digits=10)
    date=models.DateField()
    time=models.TimeField()
    trip_status=models.CharField(max_length=50,default='yet to start')
    status=models.CharField(choices=ticket_status,default=booked,max_length=3)
    seat_number = models.IntegerField()

    def __str__(self):
        return f'{self.bus_type}-{self.name}'