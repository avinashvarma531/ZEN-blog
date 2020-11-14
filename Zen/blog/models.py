from django.db import models
from django.utils.timezone import now
from ckeditor.fields import RichTextField

class Tag(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    content = RichTextField()
    date_posted = models.DateTimeField(default=now)
    tags = models.ManyToManyField(Tag)
    claps = models.IntegerField()

    def __str__(self):
        return f"{self.id} - \"{self.title}\""