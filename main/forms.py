from django import forms

from .models import Schedule


class ScheduleUpdateForm(forms.ModelForm):

    class Meta:
        model = Schedule
        fields = ('name', 'date', 'completed')
        widgets = {
            # 'date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class': 'form-control col-md-4', 'placeholder': 'Select a date', 'type': 'date'}),
            'date': forms.DateInput(attrs={'type': 'date'})
        }


class ScheduleCreateForm(forms.ModelForm):

    class Meta:
        model = Schedule
        fields = ('name', 'date', 'completed')
        widgets = {
            # 'date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class': 'form-control col-md-4', 'placeholder': 'Select a date', 'type': 'date'}),
            'date': forms.DateInput(attrs={'type': 'date'})
        }
