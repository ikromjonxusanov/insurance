from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext as _


# Create your models here.
class Post(models.Model):
    languages = (
        ('uz', 'uz'),
        ('oz', 'oz'),
        ('ru', 'ru'),
        ('en', 'en'),
    )
    language = models.CharField(max_length=255, choices=languages, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    postImage = models.ImageField(blank=True, upload_to="post")
    create_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class ServiceClass(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=5000)
    image = models.ImageField(blank=True, upload_to="servis-classes")
    create_date = models.DateField(auto_now_add=True)
    def __str__(self):
        if len(self.description) > 100: 
            return self.description[:100]+"..."
        else:
            return self.description


class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone = PhoneNumberField()
    description = models.TextField()
    read = models.BooleanField(blank=True, null=True, default=False)
    create_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name

class Location(models.Model):
    languages = (
        ('uz','uz'),
        ('oz','oz'),
        ('ru','ru'),
        ('en','en'),
    )
    regions =(
        (1, _("Toshkent shahri")),
        (2, _("Toshkent viloyati")),
        (3, _("Sirdaryo viloyati")),
        (4, _("Jizzax viloyati")),
        (5, _("Samarqand viloyati")),
        (6, _("Qashqadaryo viloyati")),
        (7, _("Surxondaryo viloyati")),
        (8, _("Buxoro viloyati")),
        (9, _("Navoiy viloyati")),
        (10,_( "Xorazm viloyati")),
        (11,_( "Andijon viloyati")),
        (12,_( "Farg'ona viloyati")),
        (13,_( "Namangan viloyati")),
        (14,_( "Qoraqalpog'iston Respublikasi")),
    )
    language = models.CharField(max_length=255, choices=languages, blank=True, null=True)
    region = models.IntegerField(choices=regions)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = PhoneNumberField()
    workDate = models.CharField(max_length=500)
    workClock = models.CharField(max_length=255)
    mapLocation = models.CharField(max_length=5000)
    def __str__(self):
        return self.name


        
