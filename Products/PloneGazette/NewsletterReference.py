# generated by ArchGenXML Fri Oct 31 14:12:55 2003
from Products.Archetypes.public import *
from OFS.PropertyManager import PropertyManager
from AccessControl import ClassSecurityInfo
try:
    from archetypes.referencebrowserwidget import ReferenceBrowserWidget
except ImportError:
    from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import *

from config import PROJECTNAME

class NewsletterReference(BaseContent, PropertyManager):

    portal_type = meta_type = 'NewsletterReference'
    archetype_name = 'Newsletter Reference'   #this name appears in the 'add' box

    security = ClassSecurityInfo()

    schema=BaseSchema  + Schema((
        TextField('description',
                  default='',
                  searchable=1,
                  isMetadata=1,
                  accessor="Description",
                  widget=TextAreaWidget(label='Description',
                                        description='An administrative summary of the content',
                                        label_msgid='label_description',
                                        description_msgid='help_description',
                                        i18n_domain="plone")
                  ),
    ReferenceField('references',
                    languageIndependent=1,
                    required=0,
                    allowed_types=(),
                    multiValued=1,
                    relationship='references',
                    widget=ReferenceBrowserWidget(label='References',
                                                  description='Select one or more remote objects',
                                                  label_msgid='label_references',
                                                  description_msgid='help_references',
                                                  i18n_domain='plonegazette',
                                                  allow_search=1,
                                                  allow_browse=1,
                                                  show_indexes=0,
                                                  ),
                ),
    ))

    # Make sure we get title-to-id generation when an object is created
    _at_rename_after_creation = True

    security.declarePublic('getObjects')
    def getObjects(self):
        """
        """
        return self.getReferences()

    # uncommant lines below when you need
    factory_type_information={
        'allowed_content_types':[],
        'global_allow' : 0,
        'content_icon':'NewsletterReference.gif',
        'immediate_view':'newsletterreference_view',
        'filter_content_types' : 0
        }

    actions=({
        'id' : 'view',
        'name' : 'View',
        'category' : 'object',
        'action' : 'string:${object_url}/NewsletterReference_view',
        'permissions' : ('View',)
        },)

registerType(NewsletterReference, PROJECTNAME)
