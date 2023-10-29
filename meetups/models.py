from django.db import models
from django.utils.text import slugify


class Location(models.Model):
    name = models.CharField(max_length=200, default='')
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.address})"


class Meetup(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, default="", blank=True, null=False, db_index=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images', default='')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='posts')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.location})"
