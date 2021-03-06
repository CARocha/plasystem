# -*- coding: UTF-8 -*-
from django.db import models
from .models import *
from django import forms
import datetime

def fecha_choice():
    years = []
    for en in Encuesta.objects.order_by('anio').values_list('anio', flat=True):
        years.append((en,en))
    return list(sorted(set(years)))

def pais():
    foo = Encuesta.objects.order_by('productor__pais').distinct().values_list('productor__pais__id', flat=True)
    return Pais.objects.filter(id__in=foo)

def organizaciones():
    foo = Encuesta.objects.order_by('productor__organizacion').distinct().values_list('productor__organizacion__id', flat=True)
    return Organizacion.objects.filter(id__in=foo)

SEXO_CHOICES = (('','------'),('Mujer','Mujer'),('Hombre','Hombre'))

EDAD_CHOICES = (('','------'),(1,'Menores de 35'),(2,'Mayores de 35'))

class ProductoresForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ProductoresForm, self).__init__(*args, **kwargs)
        self.fields['anio'] = forms.MultipleChoiceField(choices=fecha_choice(),required=True,label='Año')
        self.fields['pais'] = forms.ModelChoiceField(queryset=pais(), required=True,label='País')
        self.fields['departamento'] = forms.ModelMultipleChoiceField(queryset=Departamento.objects.all(),required=False,label='Departamento')
        self.fields['municipio'] = forms.ModelMultipleChoiceField(queryset=Municipio.objects.all(),required=False,label='Municipio')
        self.fields['organizacion'] = forms.ModelMultipleChoiceField(queryset=organizaciones(),required=False,label='Organización')
        self.fields['sexo'] = forms.ChoiceField(choices=SEXO_CHOICES,required=False,label='Sexo')
        self.fields['edad'] = forms.ChoiceField(choices=EDAD_CHOICES,required=False,label='Edad')

#validadiones
class ProduccionForm(forms.ModelForm):
    class Meta:
        model = Produccion
        fields = '__all__'

    def clean(self):
        cantidad_cosechada = self.cleaned_data.get('cantidad_cosechada')
        consumo = self.cleaned_data.get('consumo')
        procesamiento = self.cleaned_data.get('procesamiento')
        venta = self.cleaned_data.get('venta')
        sumatoria = consumo + procesamiento + venta
        if sumatoria > cantidad_cosechada:
            raise forms.ValidationError("Sumatoria (consumo + procesamiento + venta) es mayor a la cantidad cosechada")

ANIO_ACTUAL = datetime.datetime.today().year

def anio_choice():
    years = []
    for en in range(int(ANIO_ACTUAL),int(ANIO_ACTUAL)+5):
        years.append((en,en))
    return sorted(list(set(years)))

class CustomChoiceField(forms.ChoiceField):

    def __init__(self, *args, **kwargs):
        super(CustomChoiceField, self).__init__(*args, **kwargs)
        self.choices.insert(0, (None , '--------'))

class PromedioForm(forms.ModelForm):
    anio = CustomChoiceField(choices=anio_choice())
    class Meta:
        model = Promedio
        fields = '__all__'
