# flake8: noqa
from django.test import TestCase
from django.utils import timezone
from .models import Question
from django.utils import timezone

class Test(TestCase):
  def create_question(self.ques, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(self.ques=question_text, newTiem=time)




