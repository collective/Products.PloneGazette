from zope.interface import Interface


class INewsletterBTree(Interface):
    """BTree folder - holds subscribers
    """

class INewsletterTheme(Interface):
    """Base content object for newsletters and subscribers
    """

class INewsletter(Interface):
    """Base newsletter content
    """

class ISubscriber(Interface):
    """The newsletter subscriber
    """

class ISection(Interface):
    """Section inside the newsletter
    """
