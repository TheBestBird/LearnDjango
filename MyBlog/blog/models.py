from django.db import models
from django.shortcuts import reverse
import time
from django.utils.text import slugify
# Create your models here.
# After creating model use './manage.py makemigrations' to create file
# and then './manage.py migrate' to apply it

def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    rusch = "йцукенгзхфывапролджсмитбюъэ"
    engch = "ycykengzhfivaproldjsmitbyye"
    new_slug = new_slug.replace('ь', '')
    new_slug = new_slug.replace('ё', 'e')
    new_slug = new_slug.replace('ш', 'sh')
    new_slug = new_slug.replace('щ', 'sh')
    new_slug = new_slug.replace('я', 'ya')
    new_slug = new_slug.replace('ч', 'ch')
    for i in range(len(rusch)):
        new_slug = new_slug.replace(rusch[i], engch[i])
    return new_slug + '-' + str(int(time.time()))


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)        # unique=True - only unique slug and
                                                                            # automatic indexing
    body = models.TextField(blank=True, db_index=True)                      # blank=True - can be empty
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    date_pub = models.DateTimeField(auto_now_add=True)              # auto_now_add=True - data_pub will be recoded when
                                                                            # object is saved in DB

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)


# get_absolute_url is a method that makes work easier, because we can link
# to our url(which is the instance(self.slug here))
    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('post_update_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('tag_update_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
