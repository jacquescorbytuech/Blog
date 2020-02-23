#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jacques Corby-Tuech'
SITENAME = 'Jacques Corby-Tuech'
SITEURL = 'https://www.jacquescorbytuech.com'

PATH = 'content'

TIMEZONE = 'GB'

DEFAULT_LANG = 'en'

DELETE_OUTPUT_DIRECTORY = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['images']
TYPOGRIFY = False

SUMMARY_MAX_LENGTH = None

WITH_FUTURE_DATES = False

DEFAULT_DATE = 'fs'

ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

THEME = 'theme'

DISPLAY_CATEGORIES_ON_MENU = True

DISPLAY_PAGES_ON_MENU = False

USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = ''
CATEGORY_URL = '{slug}.html'
CATEGORY_SAVE_AS = '{slug}.html'

AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''

CATEGORIES_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''

TAGS_SAVE_AS = ''