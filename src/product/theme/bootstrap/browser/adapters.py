# -*- coding: utf-8 -*-
from OFS.interfaces import IItem
from plone.dexterity.interfaces import IDexterityContent
from Products.CMFPlone.browser.syndication.adapters import BaseFeedData as BaseFeedDataOriginal
from Products.CMFPlone.browser.syndication.adapters import BaseItem as BaseItemOriginal
from Products.CMFPlone.interfaces.syndication import IFeed
from Products.CMFPlone.interfaces.syndication import IFeedItem
from zope.component import adapts
from zope.interface import implementer
from zope.interface import Interface


try:
    from Products.ATContentTypes.interfaces.file import IFileContent
except ImportError:
    # or without ATContentTypes
    class IFileContent(Interface):
        pass


class BaseFeedData(BaseFeedDataOriginal):

    @property
    def has_image(self):
        return getattr(self.context, 'image', None) and self.context.image.size or None


@implementer(IFeedItem)
class BaseItem(BaseFeedData, BaseItemOriginal):
    adapts(IItem, IFeed)


class DexterityItem(BaseItem):
    adapts(IDexterityContent, IFeed)
