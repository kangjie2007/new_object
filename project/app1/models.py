from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
from django.db import models

class Account(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.username
class Account_cs(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)
    vip = models.BooleanField(default=False)
    computer1 = models.TextField()
    computer2 = models.TextField()
    computer3 = models.TextField()
    computer4 = models.TextField()
    verify_model = models.IntegerField()
    verify_RFID = models.TextField()
    verify_password = models.TextField()
    verify_gesture = models.TextField()