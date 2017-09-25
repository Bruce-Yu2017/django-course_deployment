
from __future__ import unicode_literals

from django.db import models
import re
NAME_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+$')

class UserManager(models.Manager):
	def create_validator(self, postData):
		errors = {}
		print postData
		if len(postData['name']) < 5:
			errors['name'] = "Your course name need to more than 5 characters."
		if not NAME_REGEX.match(postData['name']):
			errors['name'] = "Please enter a valid course name."
		if len(postData['description']) < 15:
			errors['desc'] = 'Your description need to more than 15 characters.'
		return errors

class Course(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)
	objects = UserManager()
