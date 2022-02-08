# -*- coding: utf-8 -*-
from plone.dexterity.content import Item
from plone.supermodel import model
from zope import schema
from zope.interface import implementer


from edi.crashcourse import _


class IMeinSkill(model.Schema):
    """ Marker interface and Dexterity Python Schema for MeinSkill
    """

    link = RelationChoice(
            title = u"Referenz zum Kurs",
            required = False
            )

    data = schema.Text(
            title = u"Lösungdaten im JSON-Format",
            required = False
            )

    notiz = schema.Text(
            title = u"Eigene Notiz zum Skill",
            required = False
            )


@implementer(IMeinSkill)
class MeinSkill(Item):
    """
    """
