## Script (Python) "safePortalMessage"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=message
##title=Returns message not in unicode but in portal encoding
##

if same_type(message, u''):
    from Products.CMFCore.utils import getToolByName
    encoding = getToolByName(context, 'plone_utils').getSiteEncoding()
    message = message.encode(encoding)

return message
