# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase

class SkillHeadlineViewlet(ViewletBase):

    def update(self):
        self.skillheadline = self.context.skillheadline
