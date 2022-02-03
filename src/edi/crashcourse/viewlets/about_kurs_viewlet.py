# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase


class AboutKursViewlet(ViewletBase):

    def render(self):
        if self.context.about:
            if self.context.about.output:
                self.about = self.context.about.output
                return super(AboutKursViewlet, self).render()
        return ''
