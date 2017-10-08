# -*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import render

from .models import Album


# Create your views here.

def index(request):
	allAlbums = Album.objects.all()
	# html = ''
	# for album in allAlbums:
	# 	url = '/userProfile/' + str(album.id) + '/'
	# 	html += '<a href="' + url + '">' + album.albumTitle + '</a><br>'
	context = {
		'allAlbums' : allAlbums,
	}
	return render(request, 'userProfile/index.html', context)


def detail(request, albumId):
	try:
		album = Album.objects.get(pk=albumId)
	except Album.DoesNotExist:
		raise Http404("Album doesn't exist")
	return render(request, 'userProfile/detail.html', {'album' : album})
