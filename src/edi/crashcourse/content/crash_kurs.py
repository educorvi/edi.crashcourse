# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.dexterity.content import Container
from plone.supermodel import model
from zope import schema
from zope.interface import implementer


from edi.crashcourse import _


class ICrashKurs(model.Schema):
    """ Marker interface and Dexterity Python Schema for CrashKurs
    """

    autoren = schema.List(title = "Kursautor:innen",
            description = "E-Mail-Adressen der Kursautor:innen (eine E-Mail-Adresse pro Zeile."
            value_type = schema.TextLine(),
            required = True
            )

    text = RichText(
            title = u"Kursinhalt",
            description = "Dieser Text wird vor der Auflistung der Skills angezeigt.",
            required = True
            )

    schlusstext = RichText(
            title = "Schlusstext",
            description = "Dieser Text wird nach der Auflistung der Skills angezeigt.",
            required = False
            )

    benutzerdaten = schema.Bool(title = "Benutzerdaten speichern",
            description = "Checkbox markieren wenn die Nutzungsdaten in den Ordnern der Benutzer\
                           gespeichert werden sollen."


@implementer(ICrashKurs)
class CrashKurs(Container):
    """
    """

    def getPortletView(self, request):
        view = ploneapi.content.get_view(name='portlet-view', context=self, request=request)
        return view.__call__()
