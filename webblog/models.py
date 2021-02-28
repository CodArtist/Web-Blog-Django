from django.db import connections,models

class Usersinfo(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=15)
    


class Blogs(models.Model):
    username=models.CharField(max_length=20)
    blog=models.TextField()
    privacy=models.BooleanField(default=False)
    images=models.ImageField(null=True,blank=True,upload_to="images")