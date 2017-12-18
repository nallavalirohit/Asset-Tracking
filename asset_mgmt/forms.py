'''
Created on Oct 23, 2012

@author: god
'''
from django.forms import ModelForm,Textarea
from UAM.models import *
from django import forms
import json
from django.contrib.admin import widgets
from django.contrib.admin.widgets import AdminDateWidget 
from asset_mgmt.models import Asset, Person, Asset_Assignment, Asset_Assignment_Employee,Asset_Track,Door
#from django.forms.models import modelformset_factory
class RegistrationForm(ModelForm):
    class Meta:
        model = Asset
        
class People_Registration(ModelForm):
    class Meta:
        model = People
        
class Asset_Assign(ModelForm):
    class Meta:
        model = Asset_Assignment
    def __init__(self, *args, **kwargs):
        super(Asset_Assign, self).__init__(*args, **kwargs)
        self.fields['Date_of_return'].widget = widgets.AdminDateWidget()
    
class Asset_Assign_Emp(ModelForm):
    class Meta:
        model = Asset_Assignment_Employee
#        raise forms.ValidationError('Something went wrong')
#    my_field = forms.DateField(widget = AdminDateWidget)


#class ContactForm(forms.Form):
#   field1 = forms.IntegerField(initial='Your name')
#   print "============"
#   def clean(self):
#       print "----------------"
#       cleaned_data = self.cleaned_data
#       f = cleaned_data.get('field1')
#       print "working"
#       if f > 10:
#          raise forms.ValidationError("Did you just enter more than 10?")
#       return cleaned_data # Never forget this otherwise you will end up with empty request.POST in the views.py.

class Door(ModelForm):
    class Meta:
        model = Door

class ContactForm(forms.Form):
    To = forms.EmailField()
    subject = forms.CharField(max_length=100)
    #message = forms.CharField( widget=forms.Textarea )
    message = forms.CharField(widget=forms.Textarea(attrs={'width':"100%", 'cols' : "20", 'rows': "5", }))
#    cc_myself = forms.BooleanField(required=False)
    
class AssetRequestForm(forms.Form):
  
    To = forms.CharField(initial='Asset Manager',widget=forms.TextInput(attrs={'readonly':'readonly'}))
    subject = forms.CharField(max_length=100)
    #message = forms.CharField( widget=forms.Textarea )
    message = forms.CharField(widget=forms.Textarea(attrs={'width':"100%", 'cols' : "20", 'rows': "5", }))
#    cc_myself = forms.BooleanField(required=False)
    
    

    
    
    
class AssetDeassignForm(forms.Form):
#    To = forms.ModelMultipleChoiceField(queryset=People_Role_Map.objects.filter(Role_Id__Role_Name = "Asset Manager"))
    To = forms.CharField(initial='Asset Manager',widget=forms.TextInput(attrs={'readonly':'readonly'}))
    subject = forms.CharField(initial='De-Assign: ')
    #message = forms.CharField( widget=forms.Textarea )
    message = forms.CharField(widget=forms.Textarea(attrs={'width':"100%", 'cols' : "20", 'rows': "5", }))
#    cc_myself = forms.BooleanField(required=False)
    
    
class SplMvmt(forms.Form):
#    To = forms.ModelMultipleChoiceField(queryset=People_Role_Map.objects.filter(Role_Id__Role_Name = "Asset Manager"))
    To = forms.CharField(initial='Asset Manager',widget=forms.TextInput(attrs={'readonly':'readonly'}))
    subject = forms.CharField(max_length=100)
    #message = forms.CharField( widget=forms.Textarea )
    message = forms.CharField(widget=forms.Textarea(attrs={'width':"100%", 'cols' : "20", 'rows': "5", }))
#    cc_myself = forms.BooleanField(required=False)
    
    
class AssetAssociation(forms.Form):
#    To = forms.ModelMultipleChoiceField(queryset=People_Role_Map.objects.filter(Role_Id__Role_Name = "Asset Manager"))
    To = forms.CharField(initial='Asset Manager',widget=forms.TextInput(attrs={'readonly':'readonly'}))
    subject = forms.CharField(max_length=100)
    #message = forms.CharField( widget=forms.Textarea )
    message = forms.CharField(widget=forms.Textarea(attrs={'width':"100%", 'cols' : "20", 'rows': "5", }))
#    cc_myself = forms.BooleanField(required=False)
    
    
class AssetDeassociation(forms.Form):
#    To = forms.ModelMultipleChoiceField(queryset=People_Role_Map.objects.filter(Role_Id__Role_Name = "Asset Manager"))
    To = forms.CharField(initial='Asset Manager',widget=forms.TextInput(attrs={'readonly':'readonly'}))
    subject = forms.CharField(max_length=100)
    #message = forms.CharField( widget=forms.Textarea )
    message = forms.CharField(widget=forms.Textarea(attrs={'width':"100%", 'cols' : "20", 'rows': "5", }))
#    cc_myself = forms.BooleanField(required=False)
    
    
class MyAsts(forms.Form):
    Assets = forms.ModelMultipleChoiceField(queryset=People_Role_Map.objects.filter(Role_Id__Role_Name = "Asset Manager"))
    

class MyAstMvts(forms.Form):
    Assets = forms.ModelMultipleChoiceField(queryset=Asset_Track.objects.all())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#ContactFormSet = modelformset_factory(Asset)


# don't deleteeeeeeeeeeeeeeeee
#class CategoryChoicesForm(forms.Form):
#    categoryoption = forms.ModelChoiceField(
#                           queryset = Category.objects.none(),
#                           required=False,label='Category')
#
#    def __init__(self, categorycreator,*args, **kwargs):
#        super(CategoryChoicesForm, self).__init__(*args, **kwargs)
#        self.creator=categorycreator
#        self.fields['categoryoption'].queryset = Category.objects.filter( 
#                                                           creator=self.creator
#                                                                        )