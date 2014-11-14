from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

class Game(models.Model):
    name = models.CharField(max_length=128,unique=True)
	
    def __unicode__(self):
        return self.name

class Score (models.Model):
    alias=models.CharField(max_length=128,unique=True)
    score=models.IntegerField(default=0)

    def __unicode__(self):
        return str(self.score)
		