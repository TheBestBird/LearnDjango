from django.db import models
from django.shortcuts import reverse
# Create your models here.
# After creating model use './manage.py makemigrations' to create file
# and then './manage.py migrate' to apply it


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)    # unique=True - only unique slug and automatic indexing
    body = models.TextField(blank=True, db_index=True)      # blank=True - can be empty
    date_pub = models.DateTimeField(auto_now_add=True)      # auto_now_add=True - data_pub will be recoded when
                                                            # object is saved in DB

# get_absolute_url is a method that makes work easier, because we can link
# to our url(which is the instance(self.slug here))
    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.title)
