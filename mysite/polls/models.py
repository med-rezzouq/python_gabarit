from django.db import models
from django.db import models
from django.utils import timezone
import datetime
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	question_type = models.CharField(max_length=100, default='polytique')
	def __str__(self):
		return self.question_text
	def was_published_recently(self):
		x=timezone.now() - datetime.timedelta(days=7)
		return self.pub_date >=x

	"""
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=30)
	was_published_recently.boolean = True
	"""
	search_fields = ['question_text']

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text

