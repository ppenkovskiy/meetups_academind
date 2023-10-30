from django.db import models
from django.utils.text import slugify
from django.utils import timezone


class Location(models.Model):
    name = models.CharField(max_length=200, default='')
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.address})"


class Participant(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Meetup(models.Model):
    title = models.CharField(max_length=100)
    organizer_email = models.EmailField(default='test@test.com')
    date = models.DateField(default=timezone.now)
    slug = models.SlugField(unique=True, default="")
    description = models.TextField()
    image = models.ImageField(upload_to='images', default='')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Participant, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.location})"
