## Script (Python) "Subscriber_edit"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=id='', email=None, format=None, active=None
##title=Edit a Subscriber
##

# if there is no id specified, keep the current one
if not id:
    id = context.getId()

translate = context.translate

new_context = context.portal_factory.doCreate(context, id)

# Custom editing method (called only for specific attributes)
new_context.edit(format=format, active=active, email=email)

msg=context.safePortalMessage(translate('Subscriber changes saved.', domain='plonegazette'))
return state.set(context=new_context, portal_status_message=msg)
