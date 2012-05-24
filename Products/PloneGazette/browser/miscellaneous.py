from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from Products.PythonScripts.standard import url_quote


class Miscellaneous(BrowserView):

    def register_newsletter(self):
        """Attribute browser view for subscribing newsletter."""
        context = aq_inner(self.context)
        form = self.request.form
        nlpath = form.get('path', None)
        if nlpath is not None:
            nlcentral = context.restrictedTraverse(nlpath)
            format = form.get('form.widgets.format')[0]
            email = form.get('form.widgets.email')
            portal_actions = getToolByName(context, 'portal_actions')
            actions = portal_actions.listFilteredActionsFor(object=nlcentral)
            url = [action['url'] for action in actions['object']
                   if action['id'] == 'subscribe'][0]
            query_url = '%s?email=%s&format=%s' % (url, url_quote(email), format)
            self.request.response.redirect(query_url)
