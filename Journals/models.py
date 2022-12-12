from django.db import models


class Journal(models.Model):
	title = models.CharField(max_length = 100)

	text_field = models.TextField(max_length = 100)

	timestamp = models.DateTimeField(auto_now_add = True)

	last_updated = models.DateTimeField(auto_now = True)

	def __str__(self):
		return "{}".format(self.title)
		return "{}".format(self.timestamp)
