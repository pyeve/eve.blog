#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Nicola Iarocci'
SITENAME = u'Eve News'
SITEURL = 'blog.python-eve.org'
#DISPLAY_PAGES_ON_MENU = False
#MENUITEMS = [('test','#')]

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Eve Website', 'http://python-eve.org'),
          ('GitHub', 'http://github.com/nicolaiarocci/eve'),
          ('IRC', 'irc://irc.freenode.net/evehq'),
          ('PyPI', 'http://pypi.python.org/pypi/Eve'),
          ('Support', 'http://python-eve.org/support.html'),
          ('Contributing', 'http://python-eve.org/contributing.html'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/nicolaiarocci'),
          ('github', 'https://github.com/nicolaiarocci/eve'),)

THEME = 'eve.iris'

EMAIL = 'eve@nicolaiarocci.com'


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
