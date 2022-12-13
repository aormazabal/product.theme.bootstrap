# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from product.theme.bootstrap.testing import PRODUCT_THEME_BOOTSTRAP_INTEGRATION_TESTING  # noqa: E501

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that product.theme.bootstrap is properly installed."""

    layer = PRODUCT_THEME_BOOTSTRAP_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if product.theme.bootstrap is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'product.theme.bootstrap'))

    def test_browserlayer(self):
        """Test that IProductThemeBootstrapLayer is registered."""
        from product.theme.bootstrap.interfaces import (
            IProductThemeBootstrapLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IProductThemeBootstrapLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):
    layer = PRODUCT_THEME_BOOTSTRAP_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['product.theme.bootstrap'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if product.theme.bootstrap is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'product.theme.bootstrap'))

    def test_browserlayer_removed(self):
        """Test that IProductThemeBootstrapLayer is removed."""
        from product.theme.bootstrap.interfaces import \
            IProductThemeBootstrapLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IProductThemeBootstrapLayer,
            utils.registered_layers())
