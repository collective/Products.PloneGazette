## Script (Python) "Section_edit"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=id='', title=None, description=None
##title=Edit content and metadata
##
if not id:
    id = context.getId()

translate = context.translate

new_context = context.portal_factory.doCreate(context, id)
new_context.edit(title=title)
new_context.plone_utils.contentEdit(new_context, id=id)

# contentEdit don't work for description as expected
new_context.setDescription(description)

msg=context.safePortalMessage(translate('Section changes saved.', domain='plonegazette'))
return state.set(context=new_context, portal_status_message=msg)
