from django.db import models
from django.utils import timezone
from baseApp.models import Company, City, Department
# Create your models here.

def get_default_city():
    return City.objects.get_or_create(city_code='ISB',
                                        city_name='Islamabad')

class Employee(models.Model):
    gender_choices = [
        ('Male','Male'),
        ('Female','Female'),
        ('Indeterminate','Indeterminate'),
    ]
    first_name = models.CharField(max_length=56)
    last_name = models.CharField(max_length=56)
    gender = models.CharField(max_length=16,choices=gender_choices)
    dob = models.DateField()
    cnic_number = models.CharField(max_length=16)
    employee_id = models.CharField(max_length=16)
    address = models.CharField(max_length=128)
    city = models.ForeignKey(City, on_delete=models.SET(get_default_city))
    phone_1 = models.CharField(max_length=128,blank=True)
    phone_2 = models.CharField(max_length=128,blank=True)
    email_1 = models.EmailField(max_length=192, blank=True)
    email_2 = models.EmailField(max_length=192, blank=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    department = models.ForeignKey(Department,on_delete=models.PROTECT)
    designation = models.CharField(max_length=128)
    joining_date = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name+self.last_name
