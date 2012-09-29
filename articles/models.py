from django.db import models



# Create your models here.
class Image(models.Model):
	url = models.URLField()
    

class Article(models.Model):
	stringID = models.CharField(max_length=500)
	title = models.CharField(max_length=255)
	url = models.URLField()
	timestamp = models.DateTimeField()
	editor = models.CharField(max_length=255)
	commentsCount = models.IntegerField(max_length=255)
	commentsURL = models.URLField()
	imageurls = models.ManyToManyField(Image)

