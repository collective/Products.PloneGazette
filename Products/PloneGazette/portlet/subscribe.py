from Acquisition import aq_inner
from Products.CMFPlone.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.PloneGazette import _
from Products.PloneGazette.interfaces import INewsletterTheme
from plone.app.portlets.portlets import base
from plone.app.vocabularies.catalog import SearchableTextSourceBinder
from plone.directives.form import Form
from plone.directives.form import Schema
from plone.portlets.interfaces import IPortletDataProvider
from plone.z3cform.layout import FormWrapper
from z3c.form import button
from z3c.form.field import Fields
from zope import schema
from zope.component import getMultiAdapter
from zope.formlib import form
from zope.interface import implements
from zope.schema import Choice
from zope.schema import Text
from zope.schema import TextLine
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


class ISubscribeNewsletterPortlet(IPortletDataProvider):
    """A portlet displaying a subscribe newsletters.
    """

    name = TextLine(
        title=_(u"Name of Portlet"),
        default=u"",
        required=False,
    )

    newsletters = schema.Choice(
        title=_(u"Newsletters"),
        description=_(u"Find the newsletter theme."),
        required=False,
        source=SearchableTextSourceBinder(
            {'object_provides': INewsletterTheme.__identifier__},
            default_query='path:',
        ),
    )


class Assignment(base.Assignment):
    implements(ISubscribeNewsletterPortlet)

    def __init__(self, name=u'', newsletters=None):
        self.name = name
        self.newsletters = newsletters

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


class ISubscribeNewsletterForm(Schema):

    email = TextLine(
        title=_(u"E-mail address"),
        required=True,
    )

    format = Choice(
        title=_(u"Format"),
        required=True,
        vocabulary=formats,
    )

    title = TextLine(
        required=False,
    )

    message = Text(
        required=False,
    )


class SubscribeNewsletterForm(Form):

    fields = Fields(ISubscribeNewsletterForm)
    ignoreContext = True
    label = _(u"")

    def __init__(self, context, request, data=None):
        """
        """
        super(Form, self).__init__(context, request)

        self.data = data

    def newslettertheme(self):
        """Returns brain of NewsletterTheme."""
        path = self.data.newsletters
        query = {
            'object_provides': INewsletterTheme.__identifier__,
        }
        if path:
            portal_state = getMultiAdapter(
                (self.context, self.request),
                name="plone_portal_state"
            )
            path = '{0}{1}'.format(
                portal_state.navigation_root_path(),
                path
            )
            query.update(
                {
                    'path': {
                        'depth': 0,
                        'query': path,
                    }
                }
            )
        catalog = getToolByName(self.context, 'portal_catalog')
        brains = catalog(query)
        if brains:
            return brains[0]

    def updateWidgets(self):
        super(self.__class__, self).updateWidgets()

        self.widgets['email'].size = 20
        newslettertheme = self.newslettertheme()
        self.widgets['format'].field.default = newslettertheme.getObject().default_format

    @property
    def action(self):
        """ Rewrite HTTP POST action.

        If the form is rendered embedded on the others pages we
        make sure the form is posted through the same view always,
        instead of making HTTP POST to the page where the form was rendered.
        """
        path = self.newslettertheme().getPath()
        return '{0}/@@register-newsletter?path={1}'.format(
            self.context.absolute_url(),
            path
        )

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

        @return: z3c.form wrapped for Plone view
        """

        context = aq_inner(self.context)

        form = SubscribeNewsletterForm(context, self.request, data=self.data)

        # Wrap a form in Plone view
        view = PortletFormView(context, self.request)
        view = view.__of__(context)  # Make sure acquisition chain is respected
        view.form_instance = form
        return view
        # return form

    def newsletters(self):
        # return self.form_wrapper.newslettertheme()
        return self.form_wrapper.form_instance.newslettertheme()

    @property
    def available(self):
        return self.newsletters()

    def title(self):
        return self.data.name or self.data.title()


class AddForm(base.AddForm):

    form_fields = form.Fields(ISubscribeNewsletterPortlet)
    label = _(u"Add Subscribe Newsletter Portlet")
    description = _(u"This portlet displays Subscribe Newsletter Portlet.")

    def __init__(self, context, request):
        super(AddForm, self).__init__(context, request)

    def create(self, data):
        return Assignment(**data)


class EditForm(base.EditForm):
    form_fields = form.Fields(ISubscribeNewsletterPortlet)
    label = _(u"Edit Subscribe Newsletter Portlet")
    description = _(u"This portlet displays Subscribe Newsletter Portlet.")
