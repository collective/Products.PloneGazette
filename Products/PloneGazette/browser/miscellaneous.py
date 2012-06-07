from Acquisition import aq_inner
from Acquisition import aq_parent
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from Products.PythonScripts.standard import url_quote

import logging


log = logging.getLogger(__name__)


class Miscellaneous(BrowserView):

    def register_newsletter(self):
        """Attribute browser view for subscribing newsletter."""
        context = aq_inner(self.context)
        form = self.request.form
        nlpath = form.get('path', None)
        if nlpath is not None:
            nlcentral = context.restrictedTraverse(nlpath)
            if nlcentral.spam_prevention() and (
                form.get('form.widgets.message') != '' or form.get('form.widgets.title') != ''
            ):
                log.warn('HONEYPOT FILLED. SUBSCRIBE REQUEST REJECTED')
                return self.request.response.redirect(context.absolute_url())
            format = form.get('form.widgets.format')[0]
            email = form.get('form.widgets.email')
            portal_actions = getToolByName(context, 'portal_actions')
            actions = portal_actions.listFilteredActionsFor(object=nlcentral)
            url = [action['url'] for action in actions['object']
                   if action['id'] == 'subscribe'][0]
            query_url = '{0}?email={1}&format={2}'.format(url, url_quote(email), format)
            if nlcentral.spam_prevention():
                query_url = '{0}&title=&message='.format(query_url)
            self.request.response.redirect(query_url)

    def unsubscribe(self):
        """Unsubscribe the subscriber."""
        context = aq_inner(self.context)
        oid = context.id
        newsletters = aq_parent(context)
        newsletters.unSubscribe(
            oid,
            REQUEST=self.request
        )
