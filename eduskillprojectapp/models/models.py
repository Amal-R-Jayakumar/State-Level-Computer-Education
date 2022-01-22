from django.db import models

# Create your models here.

class Enquiryform(models.Model):
    fname = models.CharField(max_length=100)
    email = models.EmailField(max_length=254,unique=True)
    mobile_number = models.CharField(max_length=12)
    place_of_study = models.CharField(max_length=100)
    city_live = models.CharField(max_length=200)
    course_interested = models.CharField(max_length=100)
    phone_code = models.IntegerField()
    hear = models.CharField(max_length=100,null=True, blank=True)
    mode_training = models.CharField(max_length=200,null=True, blank=True)
    other = models.CharField(max_length=300,null=True, blank=True)
    def register(self):
        self.save()
    def __str__(self):
        return f'{self.fname} -- {self.email}'
        
        
class Enrollform(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=12)
    place = models.CharField(max_length=100)
    course = models.CharField(max_length=80, null=True, blank=True)
    
    def register(self):
        self.save()
    def __str__(self):
        return f'{self.name} -- {self.mobile}'        
