from django.db import models

# Create your models here.
# class registration_data(models.Model):
#     name=models.CharField(max_length=20)
#     age=models.IntegerField(max_length=20)
#     email=models.EmailField(max_length=20)
#     pass1=models.CharField(max_length=20)
#     pass2=models.CharField(max_length=20)

#     def __str__(self):
#         return self.name

class upload_model(models.Model):
    desc = models.CharField(max_length=50)
    file = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.desc