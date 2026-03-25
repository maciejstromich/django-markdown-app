import os

from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tests.settings')

import django
django.setup()

call_command('migrate', interactive=False)

from django_markdown.tests import *  # noqa
