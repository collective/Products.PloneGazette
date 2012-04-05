from Products.CMFCore.WorkflowCore import WorkflowException
from plone.app.workflow.remap import remap_workflow

import logging
logger = logging.getLogger('PloneGazette.migration')


def _remapSubscriberWorkflow(context):
    type_ids = ('Subscriber',)
    chain = ('subscriber_workflow',)
    state_map = {'published': 'published'}
    logger.info('Remapping Subscriber workflow')
    remap_workflow(context, type_ids=type_ids, chain=chain,
                   state_map=state_map)
    logger.info('Subscriber workflow remapped')

def _ensureSubscriberFoldersPrivate(context):
    portal = context.portal_url.getPortalObject()
    workflow = portal.portal_workflow
    for brain in portal.portal_catalog(portal_type="NewsletterBTree"):
        obj = brain.getObject()
        try:
            workflow.doActionFor(obj, 'retract')
        except WorkflowException:
            pass


def migrateTo311(context):
    _remapSubscriberWorkflow(context)

def migrateTo32(context):
    _ensureSubscriberFoldersPrivate(context)
