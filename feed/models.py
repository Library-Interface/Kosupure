from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone

class Post(models.Model):
	description = models.CharField(max_length=800, blank=True)
	pic = models.ImageField(upload_to='static/images')
	date_posted = models.DateTimeField(default=timezone.now)
	user_name = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	tags = models.CharField(max_length=400, blank=True)

	def __str__(self):
		return self.description

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})

class Comments(models.Model):
	post = models.ForeignKey(Post, related_name='details', on_delete=models.CASCADE)
	user_name = models.ForeignKey(get_user_model(), related_name='details', on_delete=models.CASCADE)
	comment = models.CharField(max_length=600)
	comment_date = models.DateTimeField(default=timezone.now)

class Like(models.Model):
	user = models.ForeignKey(get_user_model(), related_name='likes', on_delete=models.CASCADE)
	post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)

	def __str__(self):
		return self.user