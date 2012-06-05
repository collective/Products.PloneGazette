"""Misc utilities"""
from AccessControl import SpecialUsers


def checkMailAddress(obj, someAddr):
    """Checks the validity of a mail address"""
    return obj.plone_utils.validateSingleEmailAddress(someAddr)


def ownerOfObject(obj):
    """Provides acl_user acquisition wrapped owner of object"""
    udb, uid = obj.getOwnerTuple()
    root = obj.getPhysicalRoot()
    udb = root.unrestrictedTraverse(udb, None)
    if udb is None:
        user = SpecialUsers.nobody
    else:
        user = udb.getUserById(uid, None)
        if user is None:
            user = SpecialUsers.nobody
        else:
            user = user.__of__(udb)
    return user
