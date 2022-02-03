# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase

def sizeof_fmt(num, suffix='Byte'):
    for unit in ['','k','M','G','T','P','E','Z']:
        if abs(num) < 1024.0:
            return "%3.2f %s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.2f %s%s" % (num, 'Y', suffix)

class OpenerVideoViewlet(ViewletBase):

    def getMedia(self):
        datei = {}
        if self.context.videofile:
            datei = {}
            datei['url'] = "%s/@@download/videofile/%s" %(self.context.absolute_url(), self.context.videofile.filename)
            if self.context.videofile.contentType.startswith('audio'):
                datei['contentType'] = 'audio/mpeg'
            else:
                datei['contentType'] = self.context.videofile.contentType
            datei['size'] = sizeof_fmt(self.context.videofile.size)
            datei['filename'] = self.context.videofile.filename
        return datei

    def render(self):
        if self.context.videofile:
            return super(OpenerVideoViewlet, self).render()
        return ''
