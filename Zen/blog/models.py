from django.db import models
from django.utils.timezone import now
from ckeditor.fields import RichTextField

class Tag(models.Model):
    '''
    Blueprint for all the tags in the blog
    Tag model or it's objects has many-to-many relationship with Post model and it's objects
    '''
    
    # properties
    name = models.CharField(max_length=15)

    # behaviours
    def __str__(self):
        return self.name

class Post(models.Model):
    '''
    Blueprint for all the posts in the blog
    Post model or it's objects has many-to-many relationship with Tag model and it's objects
    '''
    
     # properties
    title = models.CharField(max_length=100)
    description = models.TextField()
    content = RichTextField()
    date_posted = models.DateTimeField(default=now)
    tags = models.ManyToManyField(Tag)
    claps = models.IntegerField()

    # behaviours
    def __str__(self):
        return f"{self.id} - \"{self.title}\""
