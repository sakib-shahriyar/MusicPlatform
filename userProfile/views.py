# -*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Album, Song


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
	#album = Album.objects.get(pk=albumId)
	album = get_object_or_404(Album, pk=albumId)
	return render(request, 'userProfile/detail.html', {'album' : album})


def favorite(requset, albumId):
    album = get_object_or_404(Album, pk=albumId)
    try:
        selectedSong = album.song_set.get(pk=requset.POST['song'])

    except (KeyError, Song.DoesNotExist):
        return render(requset, 'userProfile/detail.html', {
            'album' : album,
            'error_message' : "You haven't selected a valid song!",
        })
    else:
        selectedSong.isFavorite = True
        selectedSong.save()
        return render(requset, 'userProfile/detail.html', {'album': album})
