## Controller Python Script "validate_subscriber_edit"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=email=None
##title=Validates a Subscriber edit_form contents
#
#
translate = context.translate

if not email:
    state.setError('email', translate('Input is required but no input given', domain='plonegazette'))
else:
    if not context.checkMailAddress(email.strip()):
        state.setError('email', translate('This is not a valid mail address', domain='plonegazette'))
    else:
        theme = context.getTheme()
        if context.email != email and  theme.alreadySubscriber(email):
            state.setError('email', translate('There is already a subscriber with this address', domain='plonegazette'))

if state.getErrors():
    msg=context.safePortalMessage(translate('Please correct the indicated errors.', domain='plonegazette'))
    return state.set(status='failure', portal_status_message=msg)
else:
    return state
