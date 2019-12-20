#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    example.py
    ~~~~~~~~~
    A simple command line application to run flask apps.
    :copyright: 2019 Miller
    :license: BSD-3-Clause
"""

# Known bugs that can't be fixed here:
#   - synopsis() cannot be prevented from clobbering existing
#     loaded modules.
#   - If the __file__ attribute on a module is a relative path and
#     the current directory is changed with os.chdir(), an incorrect
#     path will be displayed.

from flask import render_template
from . import main

# --------------------------------------------------------- common routines

@main.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@main.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    pass