from django import forms
from app.models import *

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        widgets={'password':forms.PasswordInput()}

class QuestionForm(forms.ModelForm):
    class Meta:
        model=Question
        fields='__all__'
class AnswerForm(forms.ModelForm):
    class Meta:
        model=Answer
        fields='__all__'