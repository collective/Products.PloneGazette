## Controller Python Script "validate_newslettertopic_edit"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=title=None, max_objects=''
##title=Validates a NewsletterTopic edit_form contents
#
#
translate = context.translate

if max_objects:
    try:
        test = int(max_objects)
    except:
        state.setError('max_objects', translate('You must enter here an integer', domain='plonegazette'))
if not title:
    state.setError('title', translate('Input is required but no input given', domain='plonegazette'))

if state.getErrors():
    msg=context.safePortalMessage(translate('Please correct the indicated errors.', domain='plonegazette'))
    return state.set(status='failure', portal_status_message=msg)
else:
    return state
