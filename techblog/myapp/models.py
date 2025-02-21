from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField 


class techblog(models.Model):
    title = models.CharField(max_length=100)
    discription = models.TextField()
    photo = CloudinaryField('photo', null=True, blank=True)
    # photo = models.ImageField(upload_to='pics/',null=True,blank=True)
    likes = models.PositiveIntegerField(default=0)

class Comment(models.Model):
    post = models.ForeignKey(techblog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
