#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

#SITEURL = 'http://blog.python-eve.org/'
RELATIVE_URLS = False

FEED_RSS = 'feeds/rss.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
ARTICLE_URL = '{slug}'
PAGE_URL = 'pages/{slug}'
AUTHOR_URL = 'author/{slug}'
CATEGORY_URL = 'category/{slug}'
TAG_URL = 'tag/{slug}'

#FILES_TO_COPY = (('extra/favicon.ico', 'favicon.ico'),
#                 ('extra/CNAME', 'CNAME'),)

STATIC_PATHS = [
    'extra/favicon.ico',
    'extra/CNAME'
]
