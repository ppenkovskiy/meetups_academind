from django.db import models
from django.utils.text import slugify


class Meetup(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, default="", blank=True, null=False, db_index=True)
    description = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.location}, {self.description})"

