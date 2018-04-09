__author__ = 'utente'
from django.db import connection
from django.http import HttpResponse
#from .models import  Auto, Noleggio
from collections import namedtuple
import sys


sys.getdefaultencoding()

def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


#####################################################################################################################

''' QUERY PER TROVARE LE AUTO DISPONIBILI '''

# def disponibili():                                                                        #funzionante
#     cursor = connection.cursor()
#     cursor.execute('''select targa from noleggi_auto
#                         except
#                         select  targa from noleggi_auto left join noleggi_noleggio
#                         on (noleggi_auto.id = noleggi_noleggio.fkauto_id)
#                         where datauscita is not null and dataentrata is null
#                         order by targa''')
#     elenco = []
#     rows = cursor.fetchall()
#
#     for index in range(len(rows)):            #si crea la lista 'elenco' di liste per popolare il dropdown
#         elemento = list(rows[index])
#         elemento += list(rows[index])
#         elenco.append(elemento)
#     return  elenco


def disponibili():
    cursor = connection.cursor()
    cursor.execute('''select noleggi_auto.id, targa from noleggi_auto
                        except
                        select  noleggi_auto.id, targa from noleggi_auto left join noleggi_noleggio
                        on (noleggi_auto.id = noleggi_noleggio.fkauto_id)
                        where datauscita is not null and dataentrata is null
                        ORDER BY targa''')
    elenco = []
    rows = cursor.fetchall()

    for index in range(len(rows)):
        elenco.append(rows[index])
    return  elenco

######################################################################################################################

def scrivi_disponibili(self):
    print(disponibili())




# def clean(self, value):
#     cleaned_data = self.cleaned_data
#
#
# import os
# from django.conf import settings
# from django.http import HttpResponse
# from django.template import Context
# from django.template.loader import get_template
# import datetime
# from xhtml2pdf import pisa
#
#
# def generaPDF(request):
#     data = {}
#
#     template = get_template('/home/utente/progetti/noleggi/templates/noleggi.html')
#     html  = template.render(Context(data))
#
#     file = open('test.pdf', "w+b")
#     pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=file,
#             encoding='utf-8')
#
#     file.seek(0)
#     pdf = file.read()
#     file.close()
#     return HttpResponse(pdf, mimetype='application/pdf')
