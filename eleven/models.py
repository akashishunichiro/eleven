from django.db import models

# Create your models here.

class Banner(models.Model):
    photo1 = models.ImageField(upload_to="banner/")
    photo2 = models.ImageField(upload_to="banner2/")


class Logo(models.Model):
    img = models.ImageField(upload_to="logo/")

class Eleven(models.Model):
    name = models.CharField(max_length=150)
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to ='eleven/')
    photo1 = models.ImageField(upload_to='eleven1/', null=True)
    photo2 = models.ImageField(upload_to='eleven2/', null=True)
    photo3 = models.ImageField(upload_to='eleven3/', null=True)
    priice = models.IntegerField()
    body = models.TextField()
    count = models.IntegerField()


    def __str__(self):
        return self.name
