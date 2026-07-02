import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


# Create your models here.

#class Question(models.Model):
#     question_text = models.CharField(max_length=200) # question_text, pub_date is a Field
#     pub_date = models.DateTimeField("date published")
#
#     def __str__(self):
#         return self.question_text
#
#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.choice_text
#
#     def __int__(self):
#         return self.votes
#
#     def __Question__(self):
#         return self.question

# --------------User Data----------------------
class NormalUser(AbstractUser):
    RULES = (
        ('USER', 'Normal User'),
        ('WORKER', 'Worker'),
        ('MANAGER', 'Manager'),
    )

    rule = models.CharField(max_length=10,choices=RULES,default='USER')
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    last_change = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        super().save(*args, **kwargs)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_birth_date(self):
        return f"{self.get_full_name()} - Data di Compleanno : {self.birth_date.strftime("%d/%m/%Y")}"

    def get_phone_number(self):
        return f"{self.get_full_name()} - Numero di Telefono : {self.phone_number}"


class Worker(NormalUser):
    registration_date_worker = models.DateTimeField(auto_now_add=True,)
    rule = 'WORKER'
    business = models.ForeignKey('main.Business', on_delete=models.CASCADE, related_name='workers')



    #def who_is_business_owner(self):
    #    return self.groups.filter(name='Capo Azienda').exists()

class Manager(Worker):
    registration_date_manager = models.DateTimeField(auto_now_add=True)
    rule = 'MANAGER'

# --------------Item/Product/Business Data----------------------
class Product(models.Model):
    name = models.CharField(max_length=200)
    cost = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def __int__(self):
        return self.cost


class Description(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.description

    def __int__(self):
        return self.vote

    def __Product__(self):
        return self.product

class Business(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    #TODO eventualmente da correggere
    owner = models.ForeignKey('main.NormalUser' ,on_delete=models.CASCADE, related_name='owned_businesses')

    def __str__(self):
        return f"{self.name} - {self.description}"