from django.db import models


class EntryQuerySet(models.QuerySet):

	# this function filters the query set to only return blogs that are published
	def published(self):
		return self.filter(publish=True)


class Entry(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	slug = models.SlugField(max_length=200, unique=True) # SLUG = User Friendly/URL friendly reference
	publish = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	objects = EntryQuerySet.as_manager()

	def __str__(self):
		return self.title

	# This class helps to cleanup the admin interface
	class Meta:
		verbose_name = "Blog Entry"
		verbose_name_plural = "Blog Entries"
		ordering = ["-created"]
