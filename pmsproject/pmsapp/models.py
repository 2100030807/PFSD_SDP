from django.db import models

class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50,unique=True,blank=False)
    password = models.CharField(max_length=50,blank=False)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "admin_table"



class Customers(models.Model):
    id=models.AutoField(primary_key=True)
    fullname=models.CharField(max_length=100,blank=False)
    gender_choices =  ( ("M","Male") , ("F","Female") , ("Others","Prefer not to say")  )
    gender=models.CharField(blank=False,choices=gender_choices,max_length=10)
    dateofbirth=models.CharField(max_length=20,blank=False)
    email=models.EmailField(max_length=50,blank=False,unique=True)
    username=models.CharField(max_length=50,blank=False,unique=True)
    password = models.CharField(max_length=50, blank=False)
    location = models.CharField(max_length=50, blank=False)
    contact = models.BigIntegerField(blank=False,unique=True)
    registrationtime = models.DateTimeField(blank=False,auto_now=True)

    def __str__(self):
        return self.fullname

    class Meta:
        db_table = "employee_table"

class Product(models.Model):
    id=models.AutoField(primary_key=True)
    category_choices = (("Home", "Home"), ("Jewelry", "Jewelry"), ("Electronics", "Electronics"), ("Clothes","Clothers"),("Others","Others"))
    category = models.CharField(max_length=100, blank=False,choices=category_choices)
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=200,blank=False)
    price = models.PositiveIntegerField(blank=False)
    image = models.FileField(blank=False,upload_to="productimages")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "product_table"


class Booknow(models.Model):
    fullname=models.CharField(max_length=100,blank=False)
    email=models.EmailField(max_length=50,blank=False,unique=True)
    productname=models.CharField(max_length=50,blank=False,unique=True)
    subject = models.CharField(max_length=50, blank=False)
    location = models.CharField(max_length=50, blank=False)
    contact = models.BigIntegerField(blank=False,unique=True)
    enquirytime = models.DateTimeField(blank=False,auto_now=True)



    class Meta:
        db_table = "booknow_table"