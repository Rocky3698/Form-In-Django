from django import forms
from django.forms.widgets import NumberInput
import datetime
class contactForm(forms.Form):
    name=forms.CharField(label='UserName',max_length = 10,initial='Your name')
    email=forms.EmailField(widget=forms.Textarea(attrs={'rows':1}))
    age= forms.IntegerField(required=False ,initial=20)
    comment=forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    # file=forms.FileField()
    emails=forms.EmailField()
    agree = forms.BooleanField(initial=True)
    date = forms.DateField(initial=datetime.date.today)
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    value = forms.DecimalField(required=False)
    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
    ]
    favorite_color = forms.ChoiceField(widget=forms.RadioSelect,choices=FAVORITE_COLORS_CHOICES)
    favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES)
