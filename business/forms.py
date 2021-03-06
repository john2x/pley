from django import forms
from django.forms import ModelForm, TextInput, HiddenInput
from django.forms.formsets import formset_factory

from pley.business.models import *

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('created_at', 'updated_at', 'status', 
                   'num_reviews', 'rating',
                   'lng', 'lat', 'created_by')
        widgets = {
            'name': TextInput(attrs={'class': 'required', 'minlength':'2'}),
            'website': TextInput(attrs={'class': 'url', 'minlength':'2'}),
        }

class BusinessFormSaveLatLng(forms.ModelForm):
    class Meta:
        model = Business
        fields = ('lat', 'lng')
        widgets = {
            'lat': HiddenInput(attrs={'id': 'business_lat'}),
            'lng': HiddenInput(attrs={'id': 'business_lng'}),
        }

class BusinessCategoryForm(forms.ModelForm):
    class Meta:
        model = BusinessCategory
        exclude = ('business',)

class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        exclude = ('business',)

class BusinessHoursForm(forms.ModelForm):
    class Meta:
        model = BusinessHours
        exclude = ('business',)

class BusinessDetailsForm(forms.ModelForm):
    class Meta:
        model = BusinessDetails
        exclude = ('business',)

class BusinessPaymentOptionsForm(forms.ModelForm):
    class Meta:
        model = BusinessPaymentOptions
        exclude = ('business',)

class HiddenForm(forms.Form):
    category_count = forms.IntegerField(initial='1', widget=forms.HiddenInput)
    detail_count = forms.IntegerField(initial='1', widget=forms.HiddenInput)

