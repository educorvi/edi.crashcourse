# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase

class KursTitelViewlet(ViewletBase):

    def render(self):
        if self.context.courseimage:
            return super(KursTitelViewlet, self).render()
        return ''
