from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(max_length=60)
    upwd = models.CharField(max_length=60)
    uemail = models.CharField(max_length=60)
    ushou = models.CharField(max_length=20,default='')
    uaddress = models.CharField(max_length=100,default='')
    uyoubian = models.CharField(max_length=6,default='')
    uphone = models.CharField(max_length=11,default='')
    class Meta:
        db_table = 'userinfo'