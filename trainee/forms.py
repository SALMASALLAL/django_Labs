from django import forms
from course.models import Course

class TraineeForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    age = forms.IntegerField()
    course = forms.ChoiceField(choices=[(course.id,course.name) for course in Course.objects.all()])
