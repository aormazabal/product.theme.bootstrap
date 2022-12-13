# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing.zope import WSGI_SERVER_FIXTURE

import product.theme.bootstrap


class ProductThemeBootstrapLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=product.theme.bootstrap)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'product.theme.bootstrap:default')


PRODUCT_THEME_BOOTSTRAP_FIXTURE = ProductThemeBootstrapLayer()


PRODUCT_THEME_BOOTSTRAP_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PRODUCT_THEME_BOOTSTRAP_FIXTURE,),
    name='ProductThemeBootstrapLayer:IntegrationTesting',
)


PRODUCT_THEME_BOOTSTRAP_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PRODUCT_THEME_BOOTSTRAP_FIXTURE,),
    name='ProductThemeBootstrapLayer:FunctionalTesting',
)


PRODUCT_THEME_BOOTSTRAP_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PRODUCT_THEME_BOOTSTRAP_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        WSGI_SERVER_FIXTURE,
    ),
    name='ProductThemeBootstrapLayer:AcceptanceTesting',
)
