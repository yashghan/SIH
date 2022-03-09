from django.db import models



def upload_to(instance,filename):
        return 'posts/{filename}'.format(filename=filename)

# Create your models here.
class Scheme(models.Model):        
    stateut=models.CharField(max_length=50)
    type_of_dis=models.CharField(max_length=100)
    name=models.CharField(max_length=30)
    criteria=models.CharField(max_length=30)
    typeofbenefit=models.CharField(max_length=30)
    documents=models.FileField(upload_to=upload_to)

class visitor(models.Model):
        name=models.CharField(max_length=30)
        location=models.CharField(max_length=50)
        phone=models.CharField(max_length=11)
        disability=models.CharField(max_length=20)









