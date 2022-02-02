# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase


class AboutKursViewlet(ViewletBase):

    def update(self):
        self.message = self.get_message()

    def get_message(self):
        return u'My message'

    def render(self):
        return super(AboutKursViewlet, self).render()
