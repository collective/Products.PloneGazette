## Script (Python) "NewsletterCentral_edit"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=id='', title=None, description=None, default_format='', body='', testEmail='', authorEmail='', replyto='', activationMailSubject='', activationMailTemplate='', newsletterHeader='', newsletterFooter='', newsletterStyle='', notify=0, renderTemplate='', extraRecipients='', subscriber_folder_id='', alternative_portal_url=None
##title=Edit content and metadata
##
if not id:
    id = context.getId()

translate = context.translate

new_context = context.portal_factory.doCreate(context, id)
new_context.edit(title=title,
                 default_format=default_format,
                 testEmail=testEmail,
                 authorEmail=authorEmail,
                 replyto=replyto,
                 activationMailSubject=activationMailSubject,
                 activationMailTemplate=activationMailTemplate,
                 newsletterHeader=newsletterHeader,
                 newsletterFooter=newsletterFooter,
                 newsletterStyle=newsletterStyle,
                 notify=notify,
                 renderTemplate=renderTemplate,
                 extraRecipients=extraRecipients,
                 subscriber_folder_id=subscriber_folder_id,
                 alternative_portal_url=alternative_portal_url)

new_context.plone_utils.contentEdit(new_context, 
                                    description=description)

# contentEdit don't work for description as expected
new_context.setDescription(description)
msg = context.safePortalMessage(translate('Newsletter Theme changes saved.', domain='plonegazette'))
return state.set(context=new_context, portal_status_message=msg)
