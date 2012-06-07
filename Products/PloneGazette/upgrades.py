from Products.CMFCore.utils import getToolByName

import logging

PROFILE_ID = 'profile-Products.PloneGazette:default'


def upgrade_33_to_34(context, logger=None):
    """Import cssregistry.xml and registry.xml"""
    if logger is None:
        # Called as upgrade step: define our own logger.
        logger = logging.getLogger(__name__)

    setup = getToolByName(context, 'portal_setup')
    logger.info('Reimporting cssregistry.xml.')
    setup.runImportStepFromProfile(PROFILE_ID, 'cssregistry', run_dependencies=False, purge_old=False)
    logger.info('Reimported cssregistry.xml.')

    logger.info('Reimporting registry.xml.')
    setup.runImportStepFromProfile(PROFILE_ID, 'plone.app.registry', run_dependencies=False, purge_old=False)
    logger.info('Reimported registry.xml.')
