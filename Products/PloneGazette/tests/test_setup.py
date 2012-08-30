from Products.CMFCore.utils import getToolByName
from Products.PloneGazette.tests.base import IntegrationTestCase


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

    def test_cssregistry(self):
        css = getToolByName(self.portal, 'portal_css')
        self.failUnless(css.getResource("++resource++PloneGazette.stylesheets/style.css"))

    def test_metadata__version(self):
        setup = getToolByName(self.portal, 'portal_setup')
        self.assertEqual(
            setup.getVersionForProfile('profile-Products.PloneGazette:default'),
            u'34'
        )

    def test_registry__spam_prevention__value(self):
        from zope.component import getUtility
        from plone.registry.interfaces import IRegistry
        registry = getUtility(IRegistry)
        self.assertFalse(registry['Products.PloneGazette.spam_prevention'])

    def test_registry__spam_prevention__field__instance(self):
        from zope.component import getUtility
        from plone.registry.interfaces import IRegistry
        record = getUtility(IRegistry).records.get('Products.PloneGazette.spam_prevention')
        from plone.registry.field import Bool
        self.assertTrue(isinstance(record.field, Bool))

    def test_registry__spam_prevention__field__title(self):
        from zope.component import getUtility
        from plone.registry.interfaces import IRegistry
        record = getUtility(IRegistry).records.get('Products.PloneGazette.spam_prevention')
        self.assertEqual(record.field.title, u'Spam Prevention')

    def test_registry__spam_prevention__field__description(self):
        from zope.component import getUtility
        from plone.registry.interfaces import IRegistry
        record = getUtility(IRegistry).records.get('Products.PloneGazette.spam_prevention')
        self.assertEqual(
            record.field.description,
            u'Spam Prevention for PloneGazette.'
        )

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

    def test_uninstall__cssregistry(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['PloneGazette'])
        css = getToolByName(self.portal, 'portal_css')
        self.failIf(css.getResource("++resource++PloneGazette.stylesheets/style.css"))

    def test_uninstall__registry__spam_prevention(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['PloneGazette'])
        from zope.component import getUtility
        from plone.registry.interfaces import IRegistry
        registry = getUtility(IRegistry)
        self.assertRaises(
            KeyError,
            lambda: registry['Products.PloneGazette.spam_prevention']
        )
