try:
    from AccessControl.class_init import InitializeClass
except ImportError:
    from Globals import InitializeClass
from AccessControl import ClassSecurityInfo
from AccessControl.SpecialUsers import nobody
from OFS import Folder
from Products.CMFCore.permissions import View
from Products.CMFDefault.DublinCore import DefaultDublinCoreImpl
from Products.CMFDefault.SkinnedFolder import SkinnedFolder
from Products.CMFPlone.PloneFolder import OrderedContainer
from PNLPermissions import ChangeNewsletter
from PNLBase import PNLContentBase
from zope.interface import implements

try:
    from OFS.IOrderSupport import IOrderContainer as IZopeOrderedContainer
    hasZopeOrderedSupport=1
except ImportError:
    hasZopeOrderedSupport=0
from Products.CMFPlone.interfaces.OrderedContainer import IOrderedContainer

from Products.PloneGazette.interfaces import ISection

#################
## The factory ##
#################

def addSection(self, id, title = '', REQUEST = {}):
    """
    Factory method for a Newsletter object
    """
    obj = Section(id, title)
    self._setObject(id, obj)
    getattr(self, id)._post_init()
    if REQUEST.has_key('RESPONSE'):
        return REQUEST.RESPONSE.redirect(self.absolute_url() + '/manage_main')

##############################
## The Section content type ##
##############################

class Section(SkinnedFolder, OrderedContainer, DefaultDublinCoreImpl, PNLContentBase):
    """Section class"""

    if hasZopeOrderedSupport:
        __implements__ = (IOrderedContainer, IZopeOrderedContainer)
    else:
        __implements__ = (IOrderedContainer,)


    ########################################
    ## Registration info for portal_types ##
    ########################################

    factory_type_information = {
        'id': 'Section',
        'portal_type': 'Section',
        'meta_type': 'Section',
        'description': '',
        'content_icon': 'Section.gif',
        'product': 'PloneGazette',
        'factory': 'addSection',
        'immediate_view': 'folder_listing',
        'global_allow': 0,
        'filter_content_types': 1,
        'allowed_content_types': ('Topic', 'NewsletterReference', 'NewsletterRichReference'),
        'actions': (
            {
                'id': 'view',
                'name': 'View',
                'action': 'string:${object_url}/Section_view',
                'permissions': (View, ),
                'category': 'object'
                },
            {
                'id' : 'folderlisting',
                'name' : 'Folder Listing',
                'action' : 'string:${object_url}/folder_contents',
                'permissions' : (ChangeNewsletter,)
                },
            {
                'id': 'edit',
                'name': 'Edit',
                'action': 'string:${object_url}/Section_editForm',
                'permissions': (ChangeNewsletter,),
                'category': 'object'
                },
            {
                'id': 'metadata',
                'name': 'Properties',
                'action': 'string:${object_url}/metadata_edit_form',
                'permissions': (ChangeNewsletter,),
                'category': 'object'
                },
            ),
        'aliases' : {
                'view'       : 'Section_view',
                'edit'       : 'Section_editForm',
                'metadata'   : 'metadata_edit_form',
            },
        }

    ###########################
    ## Basic class behaviour ##
    ###########################
    implements(ISection)
    manage_options = Folder.Folder.manage_options
    meta_type = factory_type_information['meta_type']

    # Standard security settings
    security = ClassSecurityInfo()
    security.declareObjectProtected(View)
    # security.declareProtected(ChangeNewsletter, "dummyMethod_editPermission")

    # Init method
    security.declarePrivate('__init__')
    def __init__(self, id, title=''):
        """__init__(self, id, title='')"""
        DefaultDublinCoreImpl.__init__(self)
        self.id = id
        self.title = title
        self.description = ""
        return

    security.declarePrivate('_post_init')
    def _post_init(self):
        """
        """
        self.indexObject()
        return

    #############################
    ## Content editing methods ##
    #############################

    security.declareProtected(ChangeNewsletter, 'edit')
    def edit(self, title=''):
        """
        object modification method
        """
        # Change attributes
        if title:
            self.title = title
        self.reindexObject()
        return

    ############################
    ## portal_catalog support ##
    ############################
    def SearchableText(self):
        """
        """
        ret = "%s %s" % (self.Title(), self.Description())
        return ret

    #############################
    ## Utilities
    ############################

    security.declarePublic('getObjects')
    def getObjects(self):
        """
        """
        hasPermission = nobody.has_permission
        result = []
        objects = [x for x in self.objectValues(('ATTopic', 'NewsletterTopic', 'NewsletterReference', 'NewsletterRichReference')) if hasPermission('View', x)]
        objects.sort(lambda a,b:cmp(self.getObjectPosition(a.getId()), self.getObjectPosition(b.getId())))
        if objects:
            for object in objects:
                sub_objects = list(object.getObjects())
                result = result + sub_objects
        return result


InitializeClass(Section)
