from django.db import models

class Employee(models.Model):

    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length= 60)
    lname = models.CharField(max_length = 60)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    phone_number = models.CharField(max_length = 11)


    def __str__(self):
        return f"{self.lname}"
