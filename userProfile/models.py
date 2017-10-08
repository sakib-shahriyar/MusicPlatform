# -*- coding: utf-8 -*-

from django.db import models
# Create your models here.

class User(models.Model):
	userName = models.CharField(max_length=16)
	fullName = models.CharField(max_length=80)
	email = models.CharField(max_length=60)
	password = models.CharField(max_length=32)
	adress = models.CharField(max_length=500)
	phone = models.CharField(max_length=14)
	userPhoto = models.CharField(max_length=1000)
	def __str__(self):
		return self.userName + ' - ' + self.fullName + ' - ' + self.email + ' - ' + self.phone


class Album(models.Model):
	artist = models.CharField(max_length=80)
	albumTitle = models.CharField(max_length=250)
	genre = models.CharField(max_length=40)
	albumLogo = models.CharField(max_length=1000)

	def __str__(self):
	 	return self.albumTitle + ' - ' + self.artist


class Song(models.Model):
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	fileType = models.CharField(max_length=10)
	songTitle = models.CharField(max_length=250)
	def __str__(self):
	 	return self.songTitle
