from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    admission_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Student
        fields = ['name', 'email', 'course', 'admission_date', 'fees']
