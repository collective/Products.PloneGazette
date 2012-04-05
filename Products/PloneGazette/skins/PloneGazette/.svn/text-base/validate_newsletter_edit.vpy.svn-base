## Controller Python Script "validate_newsletter_edit"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=title='', dateEmitted=None
##title=Validates a Newsletter edit_form contents
##
translate = context.translate

if not title:
    state.setError('title', translate('Input is required but no input given', domain='plonegazette'))
    
if dateEmitted is not None:
    dateEmitted = dateEmitted.strip()
    try:
        if dateEmitted != '':
            dateEmitted = DateTime(dateEmitted)
    except:
        dateEmitted = None
        state.setError('dateEmitted', translate('Please provide a valid date', domain='plonegazette'))


if state.getErrors():
    msg=context.safePortalMessage(translate('Please correct the indicated errors.', domain='plonegazette'))
    return state.set(status='failure', portal_status_message=msg)
else:
    return state
