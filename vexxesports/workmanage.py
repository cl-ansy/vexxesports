#!/usr/bin/env python
import os
import sys

sys.path.append('/data/django_1_4')

from django.core.management import execute_manager

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vexxesports.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)