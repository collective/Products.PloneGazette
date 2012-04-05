## Script (Python) "NewsletterTopic_edit"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=id='', title=None, description=None, meta_types=None, subjects=None, sort_on='', reverse=None, only_review_state='', max_objects=0
##title=Edit content and metadata
##
if not id:
    id = context.getId()

translate = context.translate
real_subjects = []
for subject in subjects:
    if subject != '':
        real_subjects.append(subject)

new_context = context.portal_factory.doCreate(context, id)
new_context.edit(title=title, meta_types=meta_types, subjects=real_subjects, sort_on=sort_on, reverse=reverse, only_review_state=only_review_state, max_objects=max_objects)
new_context.plone_utils.contentEdit(new_context, id=id)

# contentEdit don't work for description as expected
new_context.setDescription(description)
msg = context.safePortalMessage(translate('Newsletter Topic changes saved.', domain='plonegazette'))
return state.set(context=new_context, portal_status_message=msg)
