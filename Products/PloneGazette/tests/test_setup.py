from Products.PloneGazette.tests.base import IntegrationTestCase
from Products.CMFCore.utils import getToolByName


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_is_PloneGazette_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('PloneGazette'))

    def test_browserlayer(self):
        from Products.PloneGazette.browser.interfaces import IPloneGazetteLayer
        from plone.browserlayer import utils
        self.failUnless(IPloneGazetteLayer in utils.registered_layers())

    def test_rolemap__Manage_Subscribe_Newsletter_portlet__rolesOfPermission(self):
        permission = "Portlets: Manage Subscribe Newsletter portlet"
        roles = [
            item['name'] for item in self.portal.rolesOfPermission(
                permission
            ) if item['selected'] == 'SELECTED'
        ]
        roles.sort()
        self.assertEqual(
            roles,
            [
                'Editor',
                'Manager',
                'Site Administrator',
            ]
        )

    def test_rolemap__Manage_Subscribe_Newsletter_portlet__acquiredRolesAreUsedBy(self):
        permission = "Portlets: Manage Subscribe Newsletter portlet"
        self.assertEqual(
            self.portal.acquiredRolesAreUsedBy(permission),
            'CHECKED'
        )

    def test_uninstall__package(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['PloneGazette'])
        self.failIf(installer.isProductInstalled('PloneGazette'))

    def test_uninstall__browserlayer(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['PloneGazette'])
        from Products.PloneGazette.browser.interfaces import IPloneGazetteLayer
        from plone.browserlayer import utils
        self.failIf(IPloneGazetteLayer in utils.registered_layers())
