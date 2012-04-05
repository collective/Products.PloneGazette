#
# $Id: __init__.py 248031 2012-01-28 14:03:32Z morphex $
#

"""Newsletter Plone"""

__version__ = "$Revision: 248031 $" [11:-2]

## Archetypes import
from Products.Archetypes.public import *
from Products.Archetypes import listTypes

## CMF imports

from Products.CMFCore.utils import ContentInit
from Products.CMFCore import permissions
from Products.CMFCore.utils import registerIcon


from zope.i18nmessageid import MessageFactory
PloneGazetteFactory = MessageFactory('plonegazette')

## App imports
import NewsletterTheme, Newsletter, Subscriber, Section, NewsletterTopic
from config import PROJECTNAME
from config import product_globals

## Types to register

contentConstructors = (Newsletter.addNewsletter, Subscriber.addSubscriber, NewsletterTopic.addNewsletterTopic)
contentClasses = (Newsletter.Newsletter, Subscriber.Subscriber, NewsletterTopic.NewsletterTopic)
factoryTypes = (Newsletter.Newsletter.factory_type_information,
                Subscriber.Subscriber.factory_type_information,
                NewsletterTopic.NewsletterTopic.factory_type_information)

## Patches to apply
import patches


def initialize(context):

    import NewsletterReference
    import NewsletterRichReference
    import NewsletterBTree

    ContentInit(
        'Plone Gazette Newsletter Theme',
        content_types = (NewsletterTheme.NewsletterTheme,),
        permission = PNLPermissions.AddNewsletterTheme,
        extra_constructors = (NewsletterTheme.addNewsletterTheme,),
        fti = NewsletterTheme.NewsletterTheme.factory_type_information).initialize(context)

    ContentInit(
        'Plone Gazette Newsletter Section',
        content_types = (Section.Section,),
        permission = PNLPermissions.ChangeNewsletter,
        extra_constructors = (Section.addSection,),
        fti = Section.Section.factory_type_information).initialize(context)

    ContentInit(
        'Plone Gazette resources',
        content_types = contentClasses,
        permission = permissions.AddPortalContent,
        extra_constructors = contentConstructors,
        fti = factoryTypes).initialize(context)

    registerIcon(NewsletterTheme.NewsletterTheme, 'skins/PloneGazette/NewsletterTheme.gif', globals())
    registerIcon(Newsletter.Newsletter, 'skins/PloneGazette/Newsletter.gif', globals())
    registerIcon(Subscriber.Subscriber, 'skins/PloneGazette/Subscriber.gif', globals())
    registerIcon(Section.Section, 'skins/PloneGazette/Section.gif', globals())
    registerIcon(NewsletterTopic.NewsletterTopic, 'skins/PloneGazette/NewsletterTopic.gif', globals())

    # Archetypes init
    content_types, constructors, ftis = process_types(listTypes(PROJECTNAME), PROJECTNAME)

    ContentInit(
        PROJECTNAME + ' Content',
        content_types = content_types,
        permission = permissions.AddPortalContent,
        extra_constructors = constructors,
        fti = ftis,).initialize(context)

    return

# Plone 4 / TinyMCE compatability:
#
#  Module Products.PageTemplates.ZRPythonExpr, line 48, in __call__
#   - __traceback_info__: here.portal_tinymce.getContentType(object=here, fieldname=fname)
#  Module PythonExpr, line 1, in <expression>
#  Module Products.TinyMCE.utility, line 594, in getContentType
# TypeError: argument of type 'NoneType' is not iterable
#
# This error is raised on Plone 4.1.3 / TinyMCE 1.2.9 so we
# patch getContentType to return text/html whenever a
# Newsletter object is passed in.
#
# Handles import and attribute exceptions in case backwards
# compatability without TinyMCE is needed or TinyMCE is there
# but doesn't have getContentType defined

try:
    from Products.TinyMCE.utility import TinyMCE

    old_getContentType = TinyMCE.getContentType.im_func

    def getContentType(self, object=None, fieldname=None):
        if getattr(object, 'meta_type', None) == 'Newsletter':
            return "text/html"
        else:
            return old_getContentType(self, object=object, fieldname=fieldname)

    TinyMCE.getContentType = getContentType
except ImportError:
    pass
except AttributeError:
    pass
