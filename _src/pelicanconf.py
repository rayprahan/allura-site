#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import datetime as dt

SITENAME = 'Apache Allura'
SITEURL = 'http://allura.apache.org'
AUTHOR = ''
DESCRIPTION = 'Allura is an open source implementation of a software forge, a site that manages source code repositories, bug reports, discussions, and more for projects.'
KEYWORDS = []
DEFAULT_LANG = 'en'

PATH = 'content'
OUTPUT_PATH = '../'
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = ["_src"]  # don't delete source files
STATIC_PATHS = [
    'extra/robots.txt',
    'extra/favicon.ico',
    'extra/.htaccess',
]
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/.htaccess': {'path': '.htaccess'},
}
DIRECT_TEMPLATES = ['index', '404']

CURRENT_YEAR = dt.date.today().year

RELEASE_VERSION = '1.3.0'
RELEASE_DATE = 'Jun 2015'
DIST_URL = 'http://apache.org/dist/allura/'

FORGE_ALLURA_URL = 'https://forge-allura.apache.org/'
FEATURES_URL = '{}p/allura/wiki/Features/'.format(FORGE_ALLURA_URL)
FEATURES_COMPARISON_URL = '{}p/allura/wiki/Feature%20Comparison/'.format(FORGE_ALLURA_URL)
GIT_URL = '{}p/allura/git/'.format(FORGE_ALLURA_URL)
WIKI_URL = '{}p/allura/wiki/'.format(FORGE_ALLURA_URL)
TICKETS_URL = '{}p/allura/tickets/'.format(FORGE_ALLURA_URL)
