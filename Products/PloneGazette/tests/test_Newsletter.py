from mock import Mock

from Products.PloneGazette.Newsletter import Newsletter
from Products.PloneGazette.tests.base import IntegrationTestCase


class TestNewsletter(IntegrationTestCase):
    """ TestCase for Newsletter """

    def setUp(self):
        self.portal = self.layer['portal']
        self.newsletter = Newsletter(id='test_newsletter')
        self.newsletter.absolute_url = Mock(return_value='http://host/test_newsletter')

    def _compare_html(self, old, new):
        self.assertEqual('<div>%s</div>' % new,
                         self.newsletter.changeRelativeToAbsolute(old))

    def test_internal_link(self):
        self._compare_html(
            '<a class="internal-link" href="../folder/content">link</a>',
            '<a class="internal-link" href="http://host/folder/content">link</a>')

        self._compare_html(
            '<a href="../folder/content">link</a>',
            '<a href="http://host/folder/content">link</a>')

        self._compare_html('<a>link</a>', '<a>link</a>')

    def test_mailto(self):
        self._compare_html(
            '<a href="mailto:john@doe.com">link</a>',
            '<a href="mailto:john@doe.com">link</a>')

    def test_external_link(self):
        self._compare_html(
            '<a href="http://www.google.com">link</a>',
            '<a href="http://www.google.com">link</a>')

    def test_internal_img(self):
        self._compare_html(
            '<img src="../folder/img.jpg" />',
            '<img src="http://host/folder/img.jpg" />')

    def test_external_img(self):
        self._compare_html(
            '<img src="http://google.com/img.jpg" />',
            '<img src="http://google.com/img.jpg" />')
