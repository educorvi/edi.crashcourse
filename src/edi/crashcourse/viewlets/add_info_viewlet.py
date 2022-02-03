# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase


class AddInfoViewlet(ViewletBase):

    def render(self):
        if self.context.sonstiges:
            if self.context.sonstiges.output:
                self.addinfo = self.context.sonstiges.output
                return super(AddInfoViewlet, self).render()
        return ''
