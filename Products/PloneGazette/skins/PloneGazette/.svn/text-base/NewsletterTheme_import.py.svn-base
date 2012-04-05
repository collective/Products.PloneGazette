## Script (Python) "NewsletterTheme_import"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=file_upload
##title=
##
request = context.REQUEST
redirect = request.RESPONSE.redirect

#############################
# Form  Validation process
############################

file_upload_id = file_upload.filename
if file_upload_id[-4:] != '.csv':
    return redirect(context.absolute_url() + '/NewsletterTheme_importForm?portal_status_message=You must upload a csv file')

####################################
# Create a temp file on file system
####################################

result = context.createSubscribersFromCSV(file_upload)
msg=context.safePortalMessage(result)
return redirect(context.absolute_url() + '/NewsletterTheme_importForm?portal_status_message=%s&import=1' % msg)
