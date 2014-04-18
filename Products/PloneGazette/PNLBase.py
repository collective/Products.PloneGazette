# -*- coding: utf-8 -*-
from AccessControl import ClassSecurityInfo
from AccessControl.class_init import InitializeClass
from Products.CMFCore.utils import getToolByName


class PNLContentBase(object):
    """Shared by all that's in a NewsletterCentral
    """
    security = ClassSecurityInfo()

    security.declarePublic('getTheme')
    def getTheme(self):
        """Returns the NewsletterTheme parent object or None"""

        obj = self
        while 1:
            obj = getattr(obj, 'aq_parent', None)
            if not obj:
                return None
            meta = getattr(obj, 'meta_type', None)
            if not meta:
                return None
            if obj.meta_type == 'NewsletterTheme':
                return obj
        return

    security.declarePublic('getNewsletter')
    def getNewsletter(self):
        """Returns the NewsletterTheme parent object or None"""

        obj = self
        while obj:
            if obj.meta_type == 'Newsletter':
                return obj
            obj = obj.aq_parent
        return None

    security.declarePublic('ploneCharset')
    def ploneCharset(self):
        """The default charset of this Plone instance"""

        portal_properties = getToolByName(self, 'portal_properties')
        charset = portal_properties.site_properties.getProperty('default_charset').strip()
        return charset

InitializeClass(PNLContentBase)
