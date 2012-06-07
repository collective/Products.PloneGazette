============
PloneGazette
============

Tested with
-----------

Version above 3.2
=================

- Plone-4.1.4 [taito]

Version 3.2
===========

- Plone-4.1.3 (4112) [morphex]
- Plone-3.3 [vincentfretin]

Options
-------

- **MaildropHost** is highly recommended for mass mailing. http://www.dataflake.org/software/maildrophost

Portlet
-------

There is new style portlet called **Subscribe Newsletter Portlet**.
To make the subscribing work, you need to add NewsletterTheme first anyway.

There are also the old style portlet available.
Add Classic portlet and enter:

portlet name
  *portlet_gazette*
macro name
  *portlet*

Customize
---------

The look of the HTML newsletter
===============================

You may change globally the way the newsletter are rendered by
customizing the "newsletter_mua_formatter" template. Be very
careful to follow the instructions in the comments of this
template: "newsletter_mua_formatter" is **not** a Plone template
like the others.

You may have your own HTML newsletter formatter. Copy
"newsletter_mua_formatter" to
"/yourplone/skins/custom/my_mua_formatter" or anywhere else in the
skins path. You just need to modify your NewsletterCentral, setting
the "Newsletter render template (TALES)" field to
"nocall:here/my_mua_formatter".

Add your own recipients list
============================

Just write a script that returns a list of tuples in the form ::

    [(email, html, changeUrl), ...]

* "email" is a mail address
* "html" is "HTML" to receive HTML newsletters and "Text" for plain text newsletters
* "changeUrl" is an URL where the user may change his newsletter preferences

Example ::

    [('tom@somewhere.com',
      'HTML',
      'http://www.myplone.com/personalize_form'),
     ('jerry@elsewhere.net',
      'Text',
      'http://www.myplone.com/personalize_form'),
     ...]

Call that script "/yourplone/skins/custom/additionalSubscribers" or
anywhere else in the skins path. Modify your NewsletterCentral
setting the "Extra recipients (TALES)" field to
"nocall:here/additionalSubscribers".

In example, you could add newsletter settings in the member
preferences of your Plone site and make a script that gathers all
subscribers and related options.

IN ANY CASE, PLEASE TEST THIS SCRIPT IN A STANDALONE WAY BEFORE
USING IT IN A NEWSLETTERCENTRAL. EXCEPTIONS OR INVALID FORMATS
COULD SCREW ALL UP.

Permissions
===========

Please be sure your Subscribers folder is always **private**. Otherwise Anonymous 
will be able to see all your subscribers.

Subscriber objects itself uses one_state_workflow to be always accessible to 
anonymous (all users has to be able change own settings and we can't distinguish
between anonymous users).

Instead of using the standard CMF/Plone permissions ("Add portal
content"), PloneNewsletter comes with its own set of permissions
such you can tweak the roles that can add/manage newsletter related
resources.

* PNL Add Newsletter Theme, PNL Change Newsletter Theme
* PNL Add Newsletter, PNL Change Newsletter
* PNL Add Subscriber, PNL Change Subscriber

More informations
=================

The NewsletterReference type allows to refer any portal_type
of the site within the newsletter.

In the Newsletter the Referece has a title, a description, and
an ordered list of the referenced objects.
In our usecase we need to build a newsletter with different
reference objects. They need

* Title
* Descriptive text with richtext functionality (text is not taken
  from the referred content type)
* an optional image
* and of course the reference to a content object within the portal

The differences to the currently availablle NewsletterReference are

* richtext edit (to have more freedom of design within the newsletter)
* preview image (to provide icons for types that don't have a preview
  image, and also to provide a different format that fits the layout
  of the newsletter)

If you have any questions about NewsletterRichReference 
contact <harald.friessnegger@lovelysystems.com> (fRiSi on #lovely)
