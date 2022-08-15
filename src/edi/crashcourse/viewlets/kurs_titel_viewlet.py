# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase

class KursTitelViewlet(ViewletBase):

    def render(self):
        imageurl = self.context.absolute_url() + '/@@images/courseimage'
        self.styleattr = f"background-image: url({imageurl});"
        if self.context.courseimage:
            return super(KursTitelViewlet, self).render()
        return ''
