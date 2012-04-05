Tested and found to be working on Plone 4.1.3 (4112) tested by
[morphex] and and Plone 3.3 [vincentfretin]

This is the PloneGazette product

 Requirements

  o Zope 2.10.4 or later

  o CMFPlone 3.0

  o MaildropHost (optional) : this product is highly recommanded for
  mass mailing. http://www.dataflake.org/software/maildrophost

 Installation :

  untar the file inside the "Products" directory, restart zope, and
  install the product on your plone site with QuickInstaller or apply
  extension profile.

  **!! If you are upgrading from older versions, please read UPGRADE.TXT !!**

 Adding a newsletter subscription portlet

  Use @@manage-portlets link and add Classic portlet. Enter
  *portlet_gazette* as portlet name
  *portlet* as macro name

 Customise

  The look of the HTML newsletter

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

   Just write a script that returns a list of tuples in the form ::

    [(email, html, changeUrl), ...]

   o "email" is a mail address

   o "html" is "HTML" to receive HTML newsletters and "Text" for plaintext
     newsletters

   o "changeUrl" is an URL where the user may change his newsletter preferences

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
   USING IT IN A NEWSLETTERCENTRAL.  EXCEPTIONS OR INVALID FORMATS
   COULD SCREW ALL UP.

  Permissions

   Please be sure your Subscribers folder is always private. Otherwise Anonymous 
   will be able to see all your subscribers.
   
   Subscriber objects itself uses one_state_workflow to be always accessible to 
   anonymous (all users has to be able change own settings and we can't distinguish
   between anoynmous users).

   Instead of using the standard CMF/Plone permissions ("Add portal
   content"), PloneNewsletter comes with its own set of permisssions
   such you can tweak the roles that can add/manage newsletter related
   resources.

   o PNL Add Newsletter Theme, PNL Change Newsletter Theme

   o PNL Add Newsletter, PNL Change Newsletter

   o PNL Add Subscriber, PNL Change Subscriber

  More informations :

    The NewsletterReference type allows to refer any portal_type
    of the site within the newsletter.
 
    In the Newsletter the Referece has a title, a description, and
    an unordered list of the referenced objects
    (showing their title and descrtiption)
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
	 

   PloneGazette was originally developed by PilotSystems:
   http://www.pilotsystems.net
