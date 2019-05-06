#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jacques Corby-Tuech'
SITENAME = 'Jacques Corby-Tuech'
SITEURL = 'https://www.jacquescorbytuech.com'

PATH = 'content'

TIMEZONE = 'GB'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['images']
TYPOGRIFY = True

SUMMARY_MAX_LENGTH = None

WITH_FUTURE_DATES = False

DEFAULT_DATE = 'fs'

ARTICLE_URL = 'writing/{slug}.html'
ARTICLE_SAVE_AS = 'writing/{slug}.html'

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'