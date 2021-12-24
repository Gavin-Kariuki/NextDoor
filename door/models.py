from django.db import models
from cloudinary.models import CloudinaryField
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Neighbour(models.Model):
    name = models.CharField(max_length=60, null=True)
    description = models.CharField(max_length=400, null=True)
    location = models.CharField(max_length=200, null=True)
    population = models.IntegerField()
    image = CloudinaryField('image')
    user = models.ForeignKey('Profile', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    def create_neighbour(self):
        self.save()

    def delete_neighbour(self):
        self.delete()

    @classmethod
    def find_neighbour(cls, id):
        jirani = cls.objects.get(id = id)
        return jirani

    def update_neighbour(self, name):
        self.name = name
        self.save()

class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    post_by = models.ForeignKey(User, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbour, on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image')

    def __str__(self) -> str:
        return self.title

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()
