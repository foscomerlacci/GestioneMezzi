from django.db import models
from django.core.urlresolvers import reverse
from django.forms import inlineformset_factory
from .toolbox import disponibili
from easy_thumbnails.fields import ThumbnailerImageField
from easy_thumbnails.files import ThumbnailFile
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, SmartResize, Resize



# Create your models here.

alimentazione = (
    ('B', 'benzina'),
    ('G', 'gasolio'),
    ('M', 'metano'),
)

operatori = (
    ('01', 'operatore1'),
    ('02', 'operatore2'),
    ('03', 'operatore3'),

)


class Auto(models.Model):
    targa = models.CharField(max_length=7, null=False, unique=True)
    modello = models.CharField(max_length=50)
    alimentazione = models.CharField(max_length=1, choices=alimentazione)
    colore = models.CharField(max_length=20)
    immagine = ThumbnailerImageField(upload_to= "staticfiles/images/auto",  # il path inizia da MEDIA_URL
                                     null=True,
                                     blank= True,
                                     resize_source=dict(size=(200, 0),
                                     sharpen=True))
    #    immagine = models.ImageField(upload_to= "staticfiles/images/auto", null=True, blank= True)    # il path inizia da MEDIA_URL
    #'''qui IMAGEKIT prende in input 'immagine' e cacha il thumb opportunamente lavorato'''
    immagine_thumb = ImageSpecField(source='immagine',
                                    #processors=[ResizeToFill(50,50)],
                                    processors=[SmartResize(50,50)],
                                    format='JPEG',
                                    options={'quality':60})

    # immagine_grande = ImageSpecField(source='immagine',
    #                                  processors=[SmartResize(200,200)],
    #                                  format='JPEG',
    #                                  options={'quality':60})

    #'''qui il metodo thumbnail rende il tag per la visualizzazione del thumb, se presente, oppure rende NO PHOTO'''
    def thumbnail(self):
        if self.immagine_thumb:
            return u'<img widht=40 height=40 src="%s" />' % self.immagine_thumb.url
        else:
            return 'NO PHOTO'
    #'''qui il metodo image rende il tag per la visualizzazione di immagine, se presente, oppure rende NO PHOTO'''
    def image(self):
        if self.immagine:
            return u'<img  height=100 src= "%s" />' % self.immagine.url
        else:
            return 'NO PHOTO'

    thumbnail.short_description = ''
    thumbnail.allow_tags = True
    image.allow_tags = True


    def __str__(self):
        return self.targa

    def get_absolute_url(self):
        return reverse('noleggi:auto')

    class Meta:
        verbose_name_plural = "Auto"


class Noleggio(models.Model):
    operatore = models.CharField(max_length=2, choices=operatori)
    fkauto = models.ForeignKey(Auto, verbose_name="targa")
    datauscita = models.DateField(verbose_name="data uscita")
    dataentrata = models.DateField(verbose_name="data entrata", null=True, blank=True)

    def __str__(self):
        return self.fkauto.targa

    def get_absolute_url(self):
        return reverse('noleggi:noleggio')

    class Meta:
        verbose_name_plural = "Noleggi"
