from Products.CMFCore.WorkflowCore import WorkflowException
from plone.app.workflow.remap import remap_workflow
from Products.CMFCore.utils import getToolByName

import logging

logger = logging.getLogger('PloneGazette.migration')


PROFILE_ID = 'profile-Products.PloneGazette:default'


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


def upgrade_32_to_33(context):
    """Import factorytool.xml"""
    setup = getToolByName(context, 'portal_setup')
    logger.info('Importing factorytool.xml.')
    setup.runImportStepFromProfile(
        PROFILE_ID,
        'factorytool',
        run_dependencies=False,
        purge_old=False
    )
    logger.info('Imported factorytool.xml')
