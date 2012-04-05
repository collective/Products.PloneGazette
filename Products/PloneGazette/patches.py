from AccessControl import ClassSecurityInfo
from Products.CMFPlone.log import log


def monkeyPatch(originalClass, patchingClass):
    """Monkey patch original class with attributes from new class
       (Swiped from SpeedPack -- thanks, Christian Heimes!)

    * Takes all attributes and methods except __doc__ and __module__ from
      patching class Safes original attributes as _monkey_name
    * Overwrites/adds these attributes in original class
    """
    log("Monkeypatching class %s with class %s" %
            (originalClass.__name__,patchingClass.__name__))

    for name, newAttr in patchingClass.__dict__.items():
        # don't overwrite doc or module informations
        if name not in ('__doc__', '__module__'):
            # safe the old attribute as __monkey_name if exists
            # __dict__ doesn't show inherited attributes :/
            log(" - replacing %s" % name)
            orig = getattr(originalClass, name, None)
            if orig:
                stored_orig_name = "__monkey_" + name
                stored_orig = getattr(originalClass, stored_orig_name, None)
                # don't double-patch on refresh!
                if stored_orig is None:
                    setattr(originalClass,stored_orig_name,orig)
            # overwrite or add the new attribute
            setattr(originalClass, name, newAttr)


class TopicPatches:
    security = ClassSecurityInfo()

    security.declarePublic('getObjects')
    def getObjects(self):
        """
        """

        return self.queryCatalog(b_size=50, full_objects=True)

from Products.ATContentTypes.content.topic import ATTopic
log("Applying PloneGazette patches")
monkeyPatch(ATTopic, TopicPatches)
