from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
class Question(models.Model):
    # questionTest is the value take from CharField.
    questionText = models.CharField(max_length=200)

    # pubDate's value takes from the DateTimeField
    pubDate = models.DateTimeField('date published')

    # The __str__() method is called whenever you call str() on an object.
    # Most notably, to display an object in the Django admin site and as the value
    # inserted into a template when it displays an object.
    def __str__(self):
        return self.questionText

    # check if the question is published recently within 1 day.
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pubDate <= now


class Choice(models.Model):
    # set database ForeignKey, let it be the question value.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    # choiceText's value takes from CharField.
    choiceText = models.CharField(max_length=200)

    # votes' value takes from IntegerField.
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choiceText
