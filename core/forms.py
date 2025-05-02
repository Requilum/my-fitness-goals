from django import forms
from .models import Goal
from .models import Workout

#  goals form
class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['title', 'description', 'target', 'is_completed']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'target': forms.TextInput(attrs={'placeholder': 'e.g. Run 5k in 30 minutes'}),
        }

# workout form
class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['goal', 'date', 'activity_type', 'duration', 'sets', 'reps', 'weight', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }
