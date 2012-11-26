from Products.CMFCore.utils import getToolByName
from Products.PloneGazette.tests.base import IntegrationTestCase


class TestCase(IntegrationTestCase):
    """TestCase for upgrade step."""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_upgrade_33_to_34(self):
        css = getToolByName(self.portal, 'portal_css')
        css.unregisterResource("++resource++PloneGazette.stylesheets/style.css")
        self.failIf(css.getResource("++resource++PloneGazette.stylesheets/style.css"))

        setup = getToolByName(self.portal, 'portal_setup')
        setup.runAllImportStepsFromProfile(
            'profile-Products.PloneGazette:uninstall',
            purge_old=False,
        )
        from zope.component import getUtility
        from plone.registry.interfaces import IRegistry
        registry = getUtility(IRegistry)
        self.assertRaises(
            KeyError,
            lambda: registry['Products.PloneGazette.spam_prevention']
        )

        from Products.PloneGazette.upgrades import upgrade_33_to_34
        upgrade_33_to_34(self.portal)

        self.failUnless(css.getResource("++resource++PloneGazette.stylesheets/style.css"))

        self.assertFalse(registry['Products.PloneGazette.spam_prevention'])
