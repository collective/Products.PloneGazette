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

    def test__email_charset__has_email_charset(self):
        theme = self.createNewsletterTheme()
        self.portal.manage_changeProperties(email_charset='aaa')
        self.assertEqual(
            theme._email_charset(),
            'aaa'
        )

    def test__email_charset__no_email_charset(self):
        theme = self.createNewsletterTheme()
        self.portal.manage_delProperties(ids=['email_charset'])
        self.assertEqual(
            theme._email_charset(),
            'utf-8'
        )

    def test_subscribeFormProcess(self):
        theme = self.createNewsletterTheme()
        self.assertEqual(
            theme.subscribeFormProcess(),
            ({'email': '', 'format': 'HTML'}, {})
        )
