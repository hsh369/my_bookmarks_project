from django.db import models
from django.urls import reverse,reverse_lazy

from django.utils.text import slugify
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Package(models.Model):
    user = models.ForeignKey(User, related_name='packages', on_delete=models.CASCADE)
    name = models.CharField(max_length=256,unique=True)
    description = models.CharField(max_length=256)
    slug = models.SlugField(null=False, unique=True)
    
    def save(self,*args, **kwargs) -> None:
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("packs:package_list", kwargs={"username": self.user.username})
        
