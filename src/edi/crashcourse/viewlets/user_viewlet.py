# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase
from plone import api as ploneapi

class UserViewlet(ViewletBase):

    def update(self):
        return
        if ploneapi.user.is_anonymous():
            return
        if self.context.aq_parent.portal_type == "Crashkurs":
            if not self.context.aq_parent.benutzerdaten:
                return
            homefolder = self.getHomeFolder()
            data = self.check_and_create(homefolder)

    def getHomeFolder(self):
        current = ploneapi.user.get_current()
        pmtool = api.portal.get_tool(name='portal_membership')
        homefolder = pmtool.getHomeFolder(current.id)
        return homefolder
    
    def check_and_create(self, homefolder):
        if homefolder:
            kursuid = self.context.aq_parent.UID()
            kurstitel = self.context.aq_parent.title
            uid = self.context.UID()
            skilltitel = self.context.aq_parent.title
            kurs = getattr(homefolder, f'crashkurs-{kursuid}')
            if kurs:
                data = getattr(homefolder, f'skill-{uid}')
                if data:
                    return data #.data
                else:
                    data = ploneapi.content.create(
                        type = "MeinSkill",
                        id = f"skill-{uid}",
                        title = skilltitel,
                        container = newkurs)
                    return data #.data

            else:
                newkurs = ploneapi.content.create(
                    type = "MeinCrashKurs",
                    id = f"crashkurs-{kursid}",
                    title = kurstitel,
                    container = homefolder)
                data = ploneapi.content.create(
                    type = "MeinSkill",
                    id = f"skill-{uid}",
                    title = skilltitel,
                    container = newkurs)
                return data #.data

    def render(self):
        return ''
