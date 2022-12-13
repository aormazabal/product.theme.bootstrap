#!/bin/bash
# i18ndude should be available in current $PATH (eg by running
# ``export PATH=$PATH:$BUILDOUT_DIR/bin`` when i18ndude is located in your buildout's bin directory)
#
# For every language you want to translate into you need a
# locales/[language]/LC_MESSAGES/product.theme.bootstrap.po
# (e.g. locales/de/LC_MESSAGES/product.theme.bootstrap.po)

domain=product.theme.bootstrap

i18ndude rebuild-pot --pot $domain.pot --create $domain ../ --exclude="Products.CMFPlone.browser.syndication.templates.rss.xml.pt Products.CMFPlone.browser.syndication.templates.RSS.pt search-rss.pt"
i18ndude sync --pot $domain.pot */LC_MESSAGES/$domain.po

for po in $(find . -path '*/LC_MESSAGES/*.po'); do
  msgfmt -o ${po/%po/mo} $po;
done

