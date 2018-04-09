from django.contrib import admin
from django import forms
from django.core.urlresolvers import reverse
from django.http.request import HttpRequest
# from django.http import request
from django.core.urlresolvers import resolve
from .models import Auto, Noleggio
from .toolbox import disponibili, scrivi_disponibili
from .forms import NoleggioAdminAddForm, NoleggioAdminUpdateForm, AutoAdminAddForm, AutoAdminUpdateForm
from imagekit.admin import AdminThumbnail



# Register your models here.


class NoleggioAdmin(admin.ModelAdmin):
    list_display = ['fkauto', 'operatore', 'datauscita', 'dataentrata']
    list_filter = ['datauscita', 'operatore', 'dataentrata']
    ordering = ['-dataentrata',]
    actions = []
    actions_on_top = False
    date_hierarchy = 'datauscita'
    list_report = ['fkauto','operatore','datauscita',]

    # se si tratta di AGGIUNTA carico un form diverso!!!!!!!!
    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            return NoleggioAdminAddForm
        else:
            # return super(NoleggioAdmin, self).get_form(request, obj, **kwargs)   # funziona lo stesso
            return NoleggioAdminUpdateForm


class AutoAdmin(admin.ModelAdmin):
    list_display = ['targa', 'modello', 'alimentazione', 'colore', 'thumbnail']
    actions_on_top = False
    admin_thumbnail = AdminThumbnail(image_field='immagine')

    # se si tratta di AGGIUNTA carico un form diverso!!!!!!!!
    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            return AutoAdminAddForm
        else:
            return AutoAdminUpdateForm
        # else:
        #     # return super(NoleggioAdmin, self).get_form(request, obj, **kwargs)   # funziona lo stesso
        #     return NoleggioAdminUpdateForm

admin.site.register(Auto, AutoAdmin)
admin.site.register(Noleggio, NoleggioAdmin)
admin.site.site_header = "Gestione Noleggi"

# admin.site.site_title = "il nuovo gestionale che da oggi non avevi"
