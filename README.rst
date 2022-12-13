.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

=======================
product.theme.bootstrap
=======================

Bootstrap 4 template/forms overrides

Features
--------

- Adds rules for Bootstrap 4 forms
- Override standard view for Bootstrap 4 templates


Documentation
-------------

Include at the end of your theme rules.xml::


    <xi:include href="++theme++themebootstrap/rules.xml"/>


Installation
------------

Install product.theme.bootstrap by adding it to your buildout::

    [buildout]

    ...

    eggs =
        product.theme.bootstrap


and then running ``bin/buildout``


License
-------

The project is licensed under the GPLv2.
