from cProfile import label
from random import choice

from django import forms

from track.models import Track


class NewTrainee(forms.Form):
    name = forms.CharField(required=True,max_length=50)
    img = forms.ImageField(required=False,label='Image')
    trackobject = forms.ChoiceField(choices=Track.get_all(),label='track_id')
