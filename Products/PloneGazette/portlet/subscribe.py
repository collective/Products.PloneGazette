from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.PloneGazette import PloneGazetteFactory as _
from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider
from zope.formlib import form
from zope.interface import implements
from zope.schema import TextLine


class ISubscribeNewsletterPortlet(IPortletDataProvider):
    """A portlet displaying a subscribe newsletters.
    """

    name = TextLine(
        title=_(u"Name of Portlet"),
        default=u"",
        required=False,
    )


class Assignment(base.Assignment):
    implements(ISubscribeNewsletterPortlet)

    name = u""

    def __init__(self, name=u""):
        self.name = name

    def title(self):
        return self.name or _(u'Our newsletter')


class Renderer(base.Renderer):

    render = ViewPageTemplateFile('subscribe.pt')

    @property
    def available(self):
        return True

    def title(self):
        return self.data.name or self.data.title()


class AddForm(base.AddForm):

    form_fields = form.Fields(ISubscribeNewsletterPortlet)
    label = _(u"Add Subscribe Newsletter Portlet")
    description = _(u"This portlet displays Subscribe Newsletter Portlet.")

    def create(self, data):
        return Assignment(name=data.get('name', u""))


class EditForm(base.EditForm):
    form_fields = form.Fields(ISubscribeNewsletterPortlet)
    label = _(u"Edit Subscribe Newsletter Portlet")
    description = _(u"This portlet displays Subscribe Newsletter Portlet.")
