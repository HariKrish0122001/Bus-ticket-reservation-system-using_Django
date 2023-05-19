from django.db import models


# Create your models here.
class Bus_details(models.Model):
    bus_name = models.CharField(max_length=100)
    start_location = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    rem = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.start_location} - {self.destination}"

class User_Details(models.Model):

    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=10)
    mailid=models.CharField(max_length=50)
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
    bus_name=models.CharField(max_length=50)
    source=models.CharField(max_length=50)
    dest = models.CharField(max_length=50)
    pass_name=models.CharField(max_length=50)
    pass_gender=models.CharField(max_length=10)
    pass_age=models.IntegerField(max_length=2)
    price=models.DecimalField(decimal_places=2,max_digits=10)
    date=models.DateField()
    time=models.TimeField()
    status=models.CharField(choices=ticket_status,default=booked,max_length=3)
    seat_number = models.IntegerField()

    def __str__(self):
        return f'{self.bus_name}-{self.name}'