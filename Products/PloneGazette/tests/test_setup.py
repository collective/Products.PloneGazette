from Products.PloneGazette.tests.base import IntegrationTestCase
from Products.CMFCore.utils import getToolByName


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_is_PloneGazette_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('PloneGazette'))

    # def test_browserlayer(self):
    #     from Products.PloneGazette.browser.interfaces import IHexagonitUsernotificationsLayer
    #     from plone.browserlayer import utils
    #     self.failUnless(IHexagonitUsernotificationsLayer in utils.registered_layers())

    def test_uninstall__package(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['PloneGazette'])
        self.failIf(installer.isProductInstalled('PloneGazette'))

    # def test_uninstall__browserlayer(self):
    #     installer = getToolByName(self.portal, 'portal_quickinstaller')
    #     installer.uninstallProducts(['Products.PloneGazette'])
    #     from Products.PloneGazette.browser.interfaces import IHexagonitUsernotificationsLayer
    #     from plone.browserlayer import utils
    #     self.failIf(IHexagonitUsernotificationsLayer in utils.registered_layers())
