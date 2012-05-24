from Acquisition import aq_inner
from Products.Archetypes.Field import ImageField
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from Products.PloneGazette.interfaces import INewsletterTheme
from Products.PythonScripts.standard import url_quote
from Products.PythonScripts.standard import url_quote
from plone.app.blob.subtypes.image import ExtensionBlobField
from plone.registry.interfaces import IRegistry
from zope.annotation.interfaces import IAnnotations
from zope.component import getUtility


class Miscellaneous(BrowserView):

    def register_newsletter(self):
        """"""
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        brains = catalog(
            {
                'object_provides': INewsletterTheme.__identifier__,
            }
        )
        if brains:
            brain = brains[0]
            nlpath = brain.getPath()
            nlcentral = context.restrictedTraverse(nlpath)
            form = self.request.form
            format = form.get('form.widgets.format')[0]
            email = form.get('form.widgets.email')

            portal_actions = getToolByName(context, 'portal_actions')

            actions = portal_actions.listFilteredActionsFor(object=nlcentral)
            url = [action['url'] for action in actions['object']
                   if action['id'] == 'subscribe'][0]
            query_url = '%s?email=%s&format=%s' % (url, url_quote(email), format)
            self.request.response.redirect(query_url)
