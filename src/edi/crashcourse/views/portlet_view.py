# -*- coding: utf-8 -*-
from edi.crashcourse import _
from Products.Five.browser import BrowserView
from plone import api as ploneapi


class PortletView(BrowserView):

    def __call__(self):
        self.fc = self.context.getFolderContents()
        self.kursautoren = self.getCourseTeam()
        self.dauer = self.context.dauer
        self.skillheadline = self.context.skillheadline
        return self.index()

    def getCourseTeam(self):
        kursautoren = []
        autoren = getattr(self.context, 'autoren', [])
        if autoren:
            for username in autoren:
                entry = {}
                user = ploneapi.user.get(username=username)
                if user:
                    entry['fullname'] = user.getProperty('fullname')
                    entry['email'] = user.getProperty('email')
                    if entry:
                        kursautoren.append(entry)
        return kursautoren
