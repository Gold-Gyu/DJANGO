from django import forms
from .models import Movie

class MoviesForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = "__all__"

    release_date = forms.DateTimeField(widget=forms.NumberInput(attrs={'type': 'date'}),)
    score = forms.FloatField(widget=forms.NumberInput(attrs={'step':0.5, 'max':5, 'min':0}))
    genre = forms.CharField(widget = forms.Select(choices=[('comedy','comedy'),('thriller','thriller'),('romance','romance')]))