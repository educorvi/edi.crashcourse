# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase


class UserViewlet(ViewletBase):

    def update(self):
        self.message = self.get_message()

    def get_message(self):
        return u'''<li class="heading" i18n:translate="">
          Simple Viewlet!
        </li>'''

    def render(self):
        return self.message
