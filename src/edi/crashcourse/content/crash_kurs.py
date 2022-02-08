# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobImage, NamedBlobFile, NamedFile
from plone.app.textfield import RichText
from plone.dexterity.content import Container
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from zope import schema
from zope.interface import implementer
from plone import api as ploneapi


from edi.crashcourse import _


class ICrashKurs(model.Schema):
    """ Marker interface and Dexterity Python Schema for CrashKurs
    """

    about = RichText(
            title = "Kursbeschreibung",
            description = "Verfassen Sie hier eine allgemeine Beschreibung des Kurses.",
            required = True
            )

    lernziele = RichText(
            title = "Lernziele",
            description = "Beschreiben Sie hier die im Kurs vermittelten Kenntnisse und Fertigkeiten.",
            required = False
            )

    sonstiges = RichText(
            title = "Sonstige Informationen für den Lernenden",
            required = False
            )

    skillheadline = schema.TextLine(title = "Überschrift für die Skill-Auflistung",
            required = True,
            default = "Kursinhalte",
            )

    autoren = schema.List(title = "Kursteam",
            description = "Benutzernamen der Teammitglieder zur Anmeldung am System (z. B. E-Mail-Adresse). Ein Eintrag pro Zeile.",
            value_type = schema.TextLine(),
            required = False
            )

    benutzerdaten = schema.Bool(title = "Besuchs- und Ergebnisdaten im privaten Ordner der Lernenden speichern."
            )

    dauer = schema.TextLine(title = "Kursdauer",
            description = "Angabe zur voraussichtlichen Gesamtdauer des Kurses, z. B. ca. 10 Stunden",
            required = True,
            )

    fieldset(
        'images_video',
        label='Bilder und Video',
        fields=('courseimage', 'courseimage_caption', 'image', 'image_caption', 'videofile', 'videoembed'),
    )

    courseimage = NamedBlobImage(title=u"Titelbild",
            description = "Bild im Querformat, erscheint in der Einzelansicht über dem Titel.", required=False)

    courseimage_caption = schema.TextLine(title=u"Bildunterschrift oder Alternativtext zum Titelbild", required=False)

    image = NamedBlobImage(title="Vorschaubild",
            description = "Bild im Querformat, erscheint in der Ordnerübersicht und im Kopf des Navigationsportlets.",
            required = False)
  
    image_caption = schema.TextLine(title="Bildunterschrift oder Alternativtext zum Vorschaubild", required=False)

    videofile = NamedBlobFile(title=u"Video-Datei",
                          description=u"Hochladen einer Videodatei als Kursvorschau im *.mp4 Format.",
                          required=False)

    videoembed = schema.Text(title=u"Einbettungscode einer Videoplattform",
                        description=u"Als Alternative zur Datei kann hier der Einbettungscode einer Videoplattform\
                                    z.B. YouTube, Vimeo eingetragen werden.",
                        required=False)

@implementer(ICrashKurs)
class CrashKurs(Container):
    """
    """

    def getPortletView(self, request):
        view = ploneapi.content.get_view(name='portlet-view', context=self, request=request)
        return view.__call__()
