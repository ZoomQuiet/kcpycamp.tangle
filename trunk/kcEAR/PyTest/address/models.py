from django.db import models

# Create your models here.

class Address(models.Model):
    name = models.CharField('����', maxlength=6, unique=True)
    gender = models.CharField('�Ա�', choices=(('M', '��'), ('F', 'Ů')),
        maxlength=1, radio_admin=True)
    telphone = models.CharField('�绰', maxlength=20)
    mobile = models.CharField('�ֻ�', maxlength=11)
