from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from cloudinary.models import CloudinaryField

class Post(models.Model):
	description = models.CharField(max_length=800, blank=True)
	pic = CloudinaryField('image')
	date_posted = models.DateTimeField(default=timezone.now)
	user_name = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	tags = models.CharField(max_length=400, blank=True)
	liked_by = models.ManyToManyField(get_user_model(), related_name="likes", blank=True)
	adult_content = models.BooleanField(default=True)

	def __str__(self):
		return self.description

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})

def get_deleted_user_instance():
    return get_user_model().objects.get(username='deleted')

class Comments(models.Model):
	post = models.ForeignKey(Post, related_name='details', on_delete=models.CASCADE)
	user_name = models.ForeignKey(get_user_model(), related_name='details', on_delete=models.SET(get_deleted_user_instance))
	comment = models.CharField(max_length=600)
	comment_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.comment

class Events(models.Model):
	user = models.ForeignKey(get_user_model(), related_name='events', on_delete=models.SET(get_deleted_user_instance))
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=300, blank=True, null=True)
	date = models.DateTimeField()
	attending = models.ManyToManyField(get_user_model(), related_name="attending_events", blank=True)

	def __str__(self):
		return self.name

class EventComments(models.Model):
	events = models.ForeignKey(Events, related_name='comment_events', on_delete=models.CASCADE)
	events_user = models.ForeignKey(get_user_model(), related_name='comment_events', on_delete=models.SET(get_deleted_user_instance))
	event_comment = models.CharField(max_length=600)
	event_comment_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.event_comment

class Chat(models.Model):
	name = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	message = models.CharField(max_length=800, blank=True)
	date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.message

class Live(models.Model):
	site = models.CharField(max_length=150, blank=True)