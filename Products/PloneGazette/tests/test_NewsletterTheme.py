from Products.PloneGazette.tests.base import IntegrationTestCase
from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles


class TestNewsletterTheme(IntegrationTestCase):
    """TestCase for NewsletterTheme."""

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def createNewsletterTheme(self):
        theme = self.portal[
            self.portal.invokeFactory(
                'NewsletterTheme',
                id='newslettertheme',
            )
        ]
        theme.reindexObject()
        return theme

    def test__logCSVImportResult__empty(self):
        theme = self.createNewsletterTheme()
        self.assertEqual(theme._csv_import_log, '')
        theme. _logCSVImportResult([], [])
        self.assertEqual(theme._csv_import_log, '')

    def test__logCSVImportResult__not_empty(self):
        theme = self.createNewsletterTheme()
        self.assertEqual(theme._csv_import_log, '')
        theme. _logCSVImportResult(['AAA'], ['BBB'])
        self.assertEqual(
            theme._csv_import_log,
            '<h2>Already subscribed</h2><p>BBB</p><h2>Not valid emails</h2><p>AAA</p>'
        )

    def test_subscribeFormProcess(self):
        theme = self.createNewsletterTheme()
        self.assertEqual(
            theme.subscribeFormProcess(),
            ({'email': '', 'format': 'HTML'}, {})
        )

    def test_spam_prevention__False(self):
        theme = self.createNewsletterTheme()
        self.assertFalse(theme.spam_prevention())

    def test_spam_prevention__True(self):
        from zope.component import getUtility
        from plone.registry.interfaces import IRegistry
        registry = getUtility(IRegistry)
        registry['Products.PloneGazette.spam_prevention'] = True
        theme = self.createNewsletterTheme()
        self.assertTrue(theme.spam_prevention())
