# -*- coding: utf-8 -*-
from edi.crashcourse import _
from Products.Five.browser import BrowserView

class PortletView(BrowserView):

    def __call__(self):
        self.fc = self.context.getFolderContents()
        return self.index()
