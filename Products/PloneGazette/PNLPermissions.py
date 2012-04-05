#
# $Id: PNLPermissions.py 50069 2007-09-24 15:47:16Z naro $
#
__doc__ = """Define new permissions for newsletter handling
$Id: PNLPermissions.py 50069 2007-09-24 15:47:16Z naro $
"""
__version__ = "$Revision: 50069 $" [11:-2]

from Products.CMFCore.permissions import setDefaultRoles

# New specific permissions

AddNewsletterTheme = 'PNL Add Newsletter Theme'
ChangeNewsletterTheme = 'PNL Change Newsletter Theme'
AddNewsletter = 'PNL Add Newsletter'
ChangeNewsletter = 'PNL Change Newsletter'
AddSubscriber = 'PNL Add Subscriber'
ChangeSubscriber = 'PNL Change Subscriber'

# Default roles for those permissions
setDefaultRoles(AddNewsletterTheme, ('Manager',))
setDefaultRoles(ChangeNewsletterTheme, ('Manager', 'Owner'))
setDefaultRoles(AddNewsletter, ('Manager',))
setDefaultRoles(ChangeNewsletter, ('Manager', 'Owner'))
setDefaultRoles(AddSubscriber, ('Anonymous', 'Manager', 'Owner', 'Member'))
setDefaultRoles(ChangeSubscriber, ('Anonymous', 'Manager', 'Owner'))
