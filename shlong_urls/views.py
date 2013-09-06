from django.shortcuts import render, redirect
from shlong_urls.models import ShlongUrl
import random

def index(request):
	context = {}
	return render(request, 'shlong_urls/index.html', context)

def shorten(request):
	try:
		long_url = request.POST['url']
	except (KeyError, ShlongUrl.DoesNotExist):
		return redirect('/')
	else:
		short_url = get_short_url(long_url)
		if short_url is None:
			short_url = build_url()
			s = ShlongUrl(short_url=short_url, long_url=long_url)
			s.save()
		
		hostname = request.META['HTTP_HOST']		
		context = {'long_url': long_url,
				   'short_url': short_url,
				   'hostname':hostname }
		return render(request, 'shlong_urls/shorten.html', context)

def get_long_url(request, short_url):
	try:
		row = ShlongUrl.objects.get(short_url=short_url)
	except (KeyError, ShlongUrl.DoesNotExist):
		return redirect('/') # this should be 404
	else:
		return redirect(row.long_url)
	
	
def get_short_url(long_url):
	try:
		row = ShlongUrl.objects.get(long_url=long_url)	
	except (KeyError, ShlongUrl.DoesNotExist):
		return None
	else:
		return row.short_url
	
def build_url():
	for i in range(16):
		short_url = generate_id(i+1)
		
		try:
			row = ShlongUrl.objects.get(short_url=short_url)
		except (KeyError, ShlongUrl.DoesNotExist):
			return short_url
		else:
			continue
			
	return "Too many tries" # um...
	
def generate_id(length):
	
	chars = 'qwrtypsdfghjklzxcvbnm0123456789'
	short_id = ''
	
	while len(short_id) < length:
		start = random.randint(0, len(chars) - 1)
		short_id += chars[start:start+1]
	
	return short_id