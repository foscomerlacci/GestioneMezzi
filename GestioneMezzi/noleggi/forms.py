__author__ = 'utente'
import datetime
from django import forms
from django.http import request
from django.http.request import HttpRequest
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.models import inlineformset_factory


from .models import Noleggio, Auto
from .toolbox import disponibili
from datetimewidget.widgets import DateWidget
import bootstrap3


class NoleggioAdminUpdateForm(forms.ModelForm):

    class Meta:
        model = Noleggio
        fields = ('dataentrata',)


    # inserisco il datepicker AdminDateWidget
    dataentrata = forms.DateField(widget= AdminDateWidget, required= True, label='data entrata' )
    # dataentrata = forms.DateField(widget= AdminDateWidget, required= True, label='data entrata')


class NoleggioAdminAddForm(forms.ModelForm):
    # inizializzo il contenuto del dropdown con il contenuto della query disponibili() tutte le volte che ricarico il form
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(NoleggioAdminAddForm, self).__init__(*args,**kwargs)
        self.fields['fkauto'].choices = disponibili()

    class Meta:
        model = Noleggio
        fields = ('operatore', 'fkauto', 'datauscita' )


    # inserisco il datepicker AdminDateWidget
    datauscita = forms.DateField(widget= AdminDateWidget, required= True, label='data uscita' )
    #datauscita = forms.DateField(widget= DateWidget(bootstrap_version=3), required= True, label='data uscita' )       # inserisco il datepicker DateWidget


class AutoAdminUpdateForm(forms.ModelForm):

    class Meta:
        model = Auto
        fields = ('targa', 'modello', 'alimentazione', 'immagine')
        #exclude = ('immagine',)


    #immagine = u'<img widht=150 height=150 src="%s" />' % Auto.immagine


class AutoAdminAddForm(forms.ModelForm):

    class Meta:
        model = Auto
        fields = ('targa', 'modello', 'alimentazione', 'immagine')
        #exclude = ('immagine',)









