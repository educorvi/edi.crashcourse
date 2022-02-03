# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase


class GoalsViewlet(ViewletBase):

    def render(self):
        if self.context.lernziele:
            if self.context.lernziele.output:
                self.goals = self.context.lernziele.output
                return super(GoalsViewlet, self).render()
        return ''
