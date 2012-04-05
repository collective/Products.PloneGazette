
"""
NewsletterTopic main class
"""

# Standard Python imports

# Zope core imports
try:
    from AccessControl.class_init import InitializeClass
except ImportError:
    from Globals import InitializeClass
from AccessControl import ClassSecurityInfo
from AccessControl.SpecialUsers import nobody
from zope.interface import implements

# CMF/Plone imports
from Products.CMFCore.permissions import View, ModifyPortalContent
from Products.CMFDefault.DublinCore import DefaultDublinCoreImpl
from Products.CMFCore.PortalContent import PortalContent
from Products.CMFCore.interfaces import IContentish
from Products.CMFCore.utils import getToolByName

# Product specific imports
from PNLBase import PNLContentBase

#################
## The factory ##
#################

def addNewsletterTopic(self, id, title = '', REQUEST = {}):
    """
    Factory method for a NewsletterTopic object
    """
    obj = NewsletterTopic(id, title)
    self._setObject(id, obj)
    getattr(self, id)._post_init()
    if REQUEST.has_key('RESPONSE'):
        return REQUEST.RESPONSE.redirect(self.absolute_url() + '/manage_main')

#################################
## The Subscriber content type ##
#################################

class NewsletterTopic(PortalContent, DefaultDublinCoreImpl, PNLContentBase):
    """NewsletterTopic class"""

    ########################################
    ## Registration info for portal_types ##
    ########################################

    factory_type_information = {
        'id': 'NewsletterTopic',
        'portal_type': 'Newsletter Topic',
        'meta_type': 'NewsletterTopic',
        'description': '',
        'content_icon': 'NewsletterTopic.gif',
        'product': 'PloneGazette',
        'factory': 'addNewsletterTopic',
        'immediate_view': 'NewsletterTopic_view',
        'global_allow': 0,
        'filter_content_types': 0,
        'allowed_content_types': (),
        'actions': (
            {
                'id': 'view',
                'name': 'View',
                'action': 'string:${object_url}/NewsletterTopic_view',
                'permissions': (View,),
                'category': 'object'
                },
            {
                'id': 'edit',
                'name': 'Edit',
                'action': 'string:${object_url}/NewsletterTopic_editForm',
                'permissions': (ModifyPortalContent,),
                'category': 'object',
                },
            ),
        }

    ###########################
    ## Basic class behaviour ##
    ###########################

    implements(IContentish)

    meta_type = factory_type_information['meta_type']

    manage_options = PortalContent.manage_options

    # Standard security settings
    security = ClassSecurityInfo()
    security.declareObjectProtected(View)

    # Init method
    security.declarePrivate('__init__')
    def __init__(self, id, title=''):
        """__init__(self, id, title='')"""

        DefaultDublinCoreImpl.__init__(self)
        self.id = id
        self.title = title
        self.description = ''
        self.meta_types = []
        self.subjects = []
        self.sort_on = 'id'
        self.reverse = 0
        self.only_review_state = ''
        self.max_objects = None
        return

    security.declarePrivate('_post_init')
    def _post_init(self):
        """
        _post_init(self) => Post-init method (that is, method that is called AFTER the class has been set into the ZODB)
        """
        self.indexObject()
        return

    #############################
    ## Content editing methods ##
    #############################

    # Edit method (change this to suit your needs)
    # This edit method should only change attributes that are neither 'id' or metadatas.
    security.declareProtected(ModifyPortalContent, 'edit')
    def edit(self, title='', meta_types=None, subjects=None, sort_on='', reverse=0, only_review_state='',  max_objects=0):
        """
        edit(self, text = '') => object modification method
        """

        # Change attributes
        title = title.strip()
        if title:
            self.title = title

        self.meta_types = meta_types
        self.subjects = subjects
        self.sort_on = sort_on
        self.reverse = reverse
        self.only_review_state = only_review_state
        self.max_objects = max_objects

        # Reindex
        self.reindexObject()
        return

    security.declarePrivate('_buildQuery')
    def _buildQuery(self):
        """
        """
        query = {}
        meta_types = self.meta_types
        if meta_types:
            query['meta_type'] = tuple(meta_types)
        subjects = self.subjects
        if subjects:
            query['Subject'] = tuple(subjects)
        sort_on = self.sort_on
        if sort_on:
            query['sort_on'] = sort_on
        reverse = self.reverse
        if reverse:
            query['sort_order'] = 'reverse'
        review_state = self.only_review_state
        if review_state:
            query['review_state'] = review_state

        dateEmitted = self.getNewsletter().dateEmitted
        if dateEmitted:
            query['effective'] = {'query' : dateEmitted,
                                 'range' : 'max' }
        return query


    security.declarePublic('getAvailableTypes')
    def getAvailableTypes(self):
        """
        """
        typestool = getToolByName(self, 'portal_types')
        available_types = typestool.listContentTypes()
        result = []
        for portal_type in available_types:
            fti_object = getattr(typestool, portal_type)
            if fti_object.global_allow:
                result.append((fti_object.Metatype(), portal_type))

        return result

    security.declarePublic('getObjects')
    def getObjects(self):
        """
        """
        query = self._buildQuery()
        catalog = getToolByName(self, 'portal_catalog')
        hasPermission = nobody.has_permission
        brains = catalog.searchResults(query)

        # more than 50 objects has no sense inside a newsletter
        if len(brains) > 50:
            brains = brains[:50]
        objects = []
        for brain in brains:
            object = brain.getObject()
            if hasPermission('View', object):
                objects.append(object)

        if self.max_objects:
            max_objects = int(self.max_objects)
            if len(objects) > max_objects:
                objects =  objects[:max_objects]

        return objects

    def SearchableText(self):
        """
        """
        ret = "%s %s" % (self.Title(), self.Description())
        return ret

# Class instanciation
InitializeClass(NewsletterTopic)
