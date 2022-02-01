from zope.component import getUtility
from zope.intid.interfaces import IIntIds
from z3c.relationfield import RelationValue


def setCrashCoursePortlet(presenter, event):
    intids = getUtility(IIntIds)
    obj.cards = [RelationValue(self.intids.getId(obj))]
