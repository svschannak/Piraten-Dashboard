from django.core.management.base import BaseCommand, CommandError
from articles.models import *
import urllib2
import json
import time
from datetime import datetime, date, time
from django.utils import timezone
import copy

class Command(BaseCommand):
	help = "loads all articles from opendata"

	def handle(self, *args, **options):
		counter = 0
		json_object = json.loads(urllib2.urlopen("http://opendata.piratenpartei-mv.de/articles").read().decode('utf8'))
		#otherwise you would only have an pointer to json_object and the loop wouldn't work
		articleAPIObject = copy.deepcopy(json_object)
		#self.stdout.write("%s" % json_object)
		#loop through all articles from api
		for article in articleAPIObject:
			#self.stdout.write("%s" % len(articleAPIObject))
			#self.stdout.write("Durchlauf")
			#load all articles from db
			articlesExisting = Article.objects.all()
			#loop through all articles from db
			for existingArticle in articlesExisting:
				#check if there is already an article with the same id
				if existingArticle.stringID == article['id']:
					#if there is an already existing article, remove the article from the object
					if article in json_object:
						json_object.remove(article)
					#self.stdout.write("Treffer %s \n" % article['id'])
				else:
					#self.stdout.write("Kein Treffer %s \n" % article['id'])
					counter += 1
		#self.stdout.write("%s" % counter)
		#self.stdout.write("%s" % json_object)
		for article in json_object:
			dateTime = datetime.strptime(article['timestamp'], "%Y-%d-%m %H:%M")
			Article.objects.create(stringID = article['id'],title = article['title'],url = str(article['url']),timestamp = dateTime,editor = article['editor'],commentsCount = article['comments'],commentsURL = article['commentsurl'])
			#self.stdout.write('Artikel angelegt')