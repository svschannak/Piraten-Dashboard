# Create your views here.
from articles.models import *
from django.shortcuts import render_to_response
from django.template import RequestContext

def StartPage(request):
	articles = Article.objects.all()
	return render_to_response('front.html',
                          {'articles':articles},
                          context_instance=RequestContext(request))