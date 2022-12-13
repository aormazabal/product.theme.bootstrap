# -*- coding: utf-8 -*-
from Products.CMFPlone.browser.sitemap import SitemapView as smv
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class SitemapView(smv):

    item_template = ViewPageTemplateFile('sitemap-item.pt')

    def _renderLevel(self, children=[], level=2):
        output = ''
        for node in children:
            output += '<li class="list-group-item navTreeItem visualNoMarker">\n'
            output += self.item_template(node=node)
            children = node.get('children', [])
            if len(children):
                output += \
                    '<ul class="list-group list-group-flush pl-1 navTree navTreeLevel{0}">\n{1}\n</ul>\n'.format(
                        level, self._renderLevel(children, level + 1))
            output += '</li>\n'

        return output
