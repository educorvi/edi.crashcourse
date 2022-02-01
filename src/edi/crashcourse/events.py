from zope.component import getUtility
from zope.intid.interfaces import IIntIds
from z3c.relationfield import RelationValue


def setCrashKursPortlet(obj, event):
    intids = getUtility(IIntIds)
    obj.cards = [RelationValue(intids.getId(obj))]
