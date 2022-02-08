# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.dexterity.content import Container
from plone.supermodel import model
from zope import schema
from zope.interface import implementer


# from edi.crashcourse import _


class IMeinKurs(model.Schema):
    """ Marker interface and Dexterity Python Schema for MeinKurs
    """

    progress = schema.List(title="Fortschritt", required=False,
               value_type=schema.TextLine())


@implementer(IMeinKurs)
class MeinKurs(Container):
    """
    """
