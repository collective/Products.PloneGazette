from Acquisition import aq_inner
from Products.CMFPlone.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.PloneGazette import PloneGazetteFactory as _
from Products.PloneGazette.interfaces import INewsletterTheme
from plone.app.form.widgets.uberselectionwidget import UberSelectionWidget
from plone.app.portlets.portlets import base
from plone.app.portlets.portlets import base
from plone.app.vocabularies.catalog import SearchableTextSourceBinder
from plone.portlets.interfaces import IPortletDataProvider
from plone.portlets.interfaces import IPortletDataProvider
from plone.registry.interfaces import IRegistry
from plone.z3cform.layout import FormWrapper
from z3c.form import button
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from z3c.form.field import Fields
from z3c.form.form import Form
from zope import schema
from zope.component import getMultiAdapter
from zope.component import getUtility
from zope.formlib import form
from zope.formlib import form
from zope.interface import Interface
from zope.interface import implements
from zope.interface import implements
from zope.schema import Choice
from zope.schema import TextLine
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary
from zope.site.hooks import getSite



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


class PortletFormView(FormWrapper):
    """ Form view which renders z3c.forms embedded in a portlet.

    Subclass FormWrapper so that we can use custom frame template. """

    index = ViewPageTemplateFile("formwrapper.pt")


formats = SimpleVocabulary(
    [
        SimpleTerm(
            title=_(u"HTML"),
            value=u"HTML",
        ),
        SimpleTerm(
            title=_(u"Text"),
            value=u"Text",
        ),
    ]
)


class ISubscribeNewsletterForm(Interface):

    email = TextLine(
        title=_(u"E-mail address"),
        required=True,
    )

    format = Choice(
        title=_(u"Format"),
        required=True,
        vocabulary=formats,
    )


class SubscribeNewsletterForm(Form):

    fields = Fields(ISubscribeNewsletterForm)
    ignoreContext = True
    label = _(u"Search Event")

    def __init__(self, context, request, returnURLHint=None, full=True, data=None):
        """

        @param returnURLHint: Should we enforce return URL for this form

        @param full: Show all available fields or just required ones.
        """
        Form.__init__(self, context, request)
        self.all_fields = full

        self.returnURLHint = returnURLHint

        self.data = data

    def newslettertheme(self):
        """Returns brain of NewsletterTheme."""
        catalog = getToolByName(self.context, 'portal_catalog')
        brains = catalog(
            {
                'object_provides': INewsletterTheme.__identifier__,
            }
        )
        if brains:
            return brains[0]


    def updateWidgets(self):
        super(self.__class__, self).updateWidgets()

        self.widgets['email'].size = 20
        newslettertheme = self.newslettertheme()
        self.widgets['format'].field.default = newslettertheme.getObject().default_format

    @button.buttonAndHandler(_('Subscribe'), name='subscribe')
    def search(self, action):
        """ Form button hander. """

        data, errors = self.extractData()

        if not errors:
            pass


class Renderer(base.Renderer):

    render = ViewPageTemplateFile('subscribe.pt')

    def __init__(self, *args):
        self.assignment = args[-1]
        super(self.__class__, self).__init__(*args)
        self.form_wrapper = self.createForm()

    def createForm(self):
        """ Create a form instance.

        @return: z3c.form wrapped for Plone 3 view
        """

        context = aq_inner(self.context)

        returnURL = context.absolute_url()

        # Create a compact version of the contact form
        # (not all fields visible)
        form = SubscribeNewsletterForm(context, self.request, returnURLHint=returnURL, full=False, data=self.data)

        # Wrap a form in Plone view
        view = PortletFormView(context, self.request)
        view = view.__of__(context)  # Make sure acquisition chain is respected
        view.form_instance = form
        return view


    @property
    def available(self):
        return self.form_wrapper.form_instance.newslettertheme()

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
