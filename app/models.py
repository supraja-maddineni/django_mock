from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Question(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    question=models.CharField(max_length=500)
    def get_absolute_url(self):
        return reverse('QuestionDeatil', kwargs={'pk': self.pk})
    def __str__(self):
        return self.question

class Answer(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    question=models.ForeignKey(Question,on_delete=models.CASCADE,related_name='questions')
    answer=models.CharField(max_length=500)



