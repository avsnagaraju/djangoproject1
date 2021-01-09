from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Exfd(models.Model):
	g = [('M','Male'),('FM','FeMale')]
	d = models.OneToOneField(User,on_delete=models.CASCADE)
	age = models.IntegerField(null=True)
	gender = models.CharField(max_length=10,choices=g)
	impf = models.ImageField(upload_to="Profile/",default="mobile.jpg") 

@receiver(post_save,sender=User)
def Crpf(sender,instance,created,**kwargs):
	if created:
		Exfd.objects.create(d=instance) 

#class Mobile(models.Model):
#	mbs = [('yes','Completed'),('no','Not Completed')]
#	date = models.DateField()
#	description = models.TextField()
#	mobilestatus = models.CharField(max_length=5,choices=mbs)
#	m = models.ForeignKey(User,on_delete=models.CASCADE)