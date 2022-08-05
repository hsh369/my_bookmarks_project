from django.db import models
from django.urls import reverse
from packs.models import Package
from urllib.parse import urlparse

# Create your models here.
class Link(models.Model):
    url = models.URLField(max_length=200, unique=True)
    domain = models.URLField(max_length=200,null=True,blank=True)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    package = models.ForeignKey(Package,related_name='urls',on_delete=models.CASCADE)

    def save(self,*args, **kwargs):
        self.domain = urlparse(self.url).netloc
        super().save(*args,**kwargs)

    def __str__(self) -> str:
        return self.url

    def get_absolute_url(self):
        return reverse("packages:package_details", kwargs={"username": self.package.user.username,"slug":self.package.slug})
        