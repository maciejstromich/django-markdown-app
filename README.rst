Django-Markdown v. 0.10.0
=========================

.. _description:

**Django markdown** is django application that allows use markdown_ wysiwyg in flatpages, admin forms and other forms.
Documentaton available at readthedocs_ or github_.


.. _badges:

.. image:: https://github.com/maciejstromich/django-markdown-app/actions/workflows/tests.yml/badge.svg
    :target: https://github.com/maciejstromich/django-markdown-app/actions/workflows/tests.yml

.. image:: http://img.shields.io/pypi/v/django-markdown-app.svg?style=flat-square
    :target: https://pypi.python.org/pypi/django-markdown-app
    :alt: Version

.. image:: https://img.shields.io/badge/license-LGPL-blue.svg
    :target: http://www.gnu.org/copyleft/lesser.html
    :alt: License

.. contents::

.. _requirements:

Requirements
============

- Python >= 3.11
- Django >= 5.2
- Markdown >= 3.4
- nh3 >= 0.2.14


.. _installation:

Installation
============

**Django markdown** should be installed using pip: ::

    pip install django-markdown-app


Version compatibility
=====================

==============  ================  ===================
Django version  Python version    django-markdown-app
==============  ================  ===================
5.2             3.11 - 3.14       0.10.0
2.0 - 2.2      3.6 - 3.7         0.9.7
2.0 - 2.1      3.6 - 3.7         0.9.6
1.8 or later    2.7, 3.x         0.9.3.1
prior to 1.8    2.7               0.8.5.1
==============  ================  ===================


Setup
=====

.. note:: 'django_markdown' require 'django.contrib.staticfiles' in INSTALLED_APPS

- Add 'django_markdown' to INSTALLED_APPS ::

    INSTALLED_APPS += [ 'django_markdown', ]


- Add django_markdown urls to base urls ::

    path('markdown/', include( 'django_markdown.urls')),


Use django_markdown
===================

#) Models: ::

    from django_markdown.models import MarkdownField


    class MyModel(models.Model):
        content = MarkdownField()


#) Custom forms: ::

    from django_markdown.fields import MarkdownFormField
    from django_markdown.widgets import MarkdownWidget


    class MyCustomForm(forms.Form):
        content = forms.CharField(widget=MarkdownWidget())
        content2 = MarkdownFormField()


#) Custom admins: ::

    from django_markdown.admin import MarkdownModelAdmin

    admin.site.register(MyModel, MarkdownModelAdmin)


#) Admin Overrides: (If you don't want to subclass package ModelAdmin's) ::

    from django.contrib import admin

    class YourModelAdmin(admin.ModelAdmin):
        formfield_overrides = {MarkdownField: {'widget': AdminMarkdownWidget}}


#) Flatpages: ::

    # in your project main urls
    from django_markdown import flatpages
    ...
    flatpages.register()
    urlpatterns += [ path('admin/', admin.site.urls), ]


#) Template tags: ::

    <textarea name="test" id="new"></textarea>
    {% markdown_editor "#new" %}
    {% markdown_media %}


Settings
========

**MARKDOWN_EDITOR_SETTINGS** - holds the extra parameters set to be passed to ``textarea.markItUp()``

**MARKDOWN_EDITOR_SKIN** - skin option, default value is ``markitup``

Example: `settings.py` ::

    MARKDOWN_EDITOR_SKIN = 'simple'

**MARKDOWN_EXTENSIONS** - optional list of extensions passed to Markdown.

Officially supported extensions could be found
at https://python-markdown.github.io/extensions/#officially-supported-extensions

Example: `settings.py` ::

    MARKDOWN_EXTENSIONS = ['extra']

**MARKDOWN_EXTENSION_CONFIGS** - configure extensions

**MARKDOWN_PREVIEW_TEMPLATE** - template for preview a markdown. By default `django_markdown/preview.css`

**MARKDOWN_STYLE** - path to preview styles. By default `django_markdown/preview.css`

**MARKDOWN_SET_PATH** - path to folder with sets. By default `django_markdown/sets`

**MARKDOWN_SET_NAME** - name for current set. By default `markdown`.

**MARKDOWN_PROTECT_PREVIEW** - protect preview url for staff only


Development
===========

A Docker-based development environment is provided::

    make build    # build the Docker image
    make shell    # open a bash shell in the container
    make test     # run tox tests
    make lint     # run ruff linter
    make format   # run ruff formatter


Changes
=======

Make sure you've read the changes_ document if you are upgrading from previous version.


Bug tracker
===========

If you have any suggestions, bug reports or
annoyances please report them to the issue tracker
at https://github.com/maciejstromich/django-markdown-app/issues


Contributing
============

Development of django-markdown happens at github: https://github.com/maciejstromich/django-markdown-app

All changes should include tests and pass ruff_ linting.


Contributors
============

* klen_ (Kirill Klenov)

* yavorskiy_ (Sergii Iavorskyi)

* contributors_ (Other contributors)


License
=======

Licensed under a `GNU lesser general public license`_.


Copyright
=========

Copyright (c) 2011 Kirill Klenov (horneds@gmail.com)

Markitup_:
    (c) 2008 Jay Salvat
    http://markitup.jaysalvat.com/


.. _GNU lesser general public license: https://www.gnu.org/copyleft/lesser.html
.. _readthedocs: https://django-markdown-app.readthedocs.io
.. _Markitup: https://markitup.jaysalvat.com
.. _github: https://github.com/maciejstromich/django-markdown-app
.. _klen: https://github.com/klen
.. _yavorskiy: https://github.com/yavorskiy
.. _markdown: https://python-markdown.github.io
.. _changes: https://django-markdown-app.readthedocs.io/en/latest/changes.html
.. _ruff: https://github.com/astral-sh/ruff
.. _contributors: CONTRIBUTORS.rst
