from django import forms
from django.shortcuts import render
from django.core import exceptions, validators


class FormProduto(forms.Form):
    name = forms.CharField(validators=[validators.MaxLengthValidator(10)])
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
    quantidade = forms.IntegerField()
    cor =  forms.CharField()
    #acumulado = forms.IntegerField
  
class FormComponente(forms.Form):
    name = forms.CharField()
    quantidade = forms.BooleanField()
    cor =  forms.CharField(widget = forms.Textarea)

class FormCliente(forms.Form):
    name = forms.CharField()
    codigo = forms.IntegerField()


class Produto(Form.ModelForm):
    class Meta:
        model = MyModels
        fields = "_all_",