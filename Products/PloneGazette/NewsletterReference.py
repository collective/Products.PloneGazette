from AccessControl import ClassSecurityInfo
from OFS.PropertyManager import PropertyManager
from Products.Archetypes.public import BaseContent
from Products.Archetypes.public import BaseSchema
from Products.Archetypes.public import Schema
from Products.Archetypes.public import TextAreaWidget
from Products.Archetypes.public import TextField
from Products.Archetypes.public import registerType
from Products.OrderableReferenceField import OrderableReferenceField
from Products.PloneGazette.config import PROJECTNAME
from archetypes.referencebrowserwidget import ReferenceBrowserWidget

NewsletterReferenceSchema = BaseSchema.copy() + Schema((
    TextField(
        'description',
        default='',
        searchable=1,
        isMetadata=1,
        accessor="Description",
        widget=TextAreaWidget(
            description='An administrative summary of the content',
            description_msgid='help_description',
            i18n_domain="plone",
            label='Description',
            label_msgid='label_description',
        )
    ),
    OrderableReferenceField(
        'references',
        languageIndependent=1,
        required=0,
        allowed_types=(),
        multiValued=1,
        relationship='references',
        widget=ReferenceBrowserWidget(
            allow_browse=1,
            allow_search=1,
            allow_sorting=1,
            description='Select one or more remote objects',
            description_msgid='help_references',
            i18n_domain='plonegazette',
            label='References',
            label_msgid='label_references',
            show_indexes=0,
        )
    ),
))


class NewsletterReference(BaseContent, PropertyManager):

    portal_type = meta_type = 'NewsletterReference'
    archetype_name = 'Newsletter Reference'  # this name appears in the 'add' box

    schema = NewsletterReferenceSchema
    security = ClassSecurityInfo()

    # Make sure we get title-to-id generation when an object is created
    _at_rename_after_creation = True

    security.declarePublic('getObjects')
    def getObjects(self):
        """
        """
        # return self.getReferences()
        return self.getField('references', self).get(self)

    # uncommant lines below when you need
    factory_type_information = {
        'allowed_content_types': [],
        'global_allow': 0,
        'content_icon': 'NewsletterReference.gif',
        'immediate_view': 'newsletterreference_view',
        'filter_content_types': 0
        }

    actions = ({
        'id': 'view',
        'name': 'View',
        'category': 'object',
        'action': 'string:${object_url}/NewsletterReference_view',
        'permissions': ('View',)
        },)


registerType(NewsletterReference, PROJECTNAME)
