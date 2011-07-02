from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    return render_to_response("main.html", 
							  context_instance=RequestContext(request))

def ob_start(request):
	return HttpResponseRedirect("http://blog.sirvaliance.com/sir-valiance-start")


def ob_mobius(request):
	return HttpResponseRedirect("http://blog.sirvaliance.com/mobius")


def ob_quantico(request):
	return HttpResponseRedirect("http://blog.sirvaliance.com/sir-valiance-quantico")


def ob_fresh(request):
	return HttpResponseRedirect("http://blog.sirvaliance.com/a-fresh-start")


def robots(reqeust):
	return HttpResponse("User-agent: * \r\n Disallow:")

def four(request):
	return render_to_response('404.html',
							  context_instance=RequestContext(request))


