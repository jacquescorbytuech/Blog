#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from distutils.sysconfig import get_python_lib

AUTHOR = 'Jacques Corby-Tuech'
SITENAME = 'Jacques Corby-Tuech'
SITEURL = 'https://www.jacquescorbytuech.com'

PATH = 'content'

ARTICLE_PATHS = ['links', 'reading', 'writing']

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


PLUGIN_PATHS = [get_python_lib()]
PLUGINS = [
            'pelican_image_process',
          ]

IMAGE_PROCESS = {
    'crisp': {'type': 'responsive-image',
              'srcset': [('1x', ["scale_in 800 600 True"]),
                         ('2x', ["scale_in 1600 1200 True"]),
                         ('4x', ["scale_in 3200 2400 True"]),
                         ],
               'default': '1x',
             },
    'large-photo': {'type': 'responsive-image',
                    'sizes': '(min-width: 1200px) 800px, (min-width: 992px) 650px, \
                              (min-width: 768px) 718px, 100vw',
                    'srcset': [('600w', ["scale_in 600 450 True"]),
                               ('800w', ["scale_in 800 600 True"]),
                               ('1600w', ["scale_in 1600 1200 True"]),
                               ],
                    'default': '800w',
                   },
    'signature': {'type': 'responsive-image',
              'srcset': [('180w', ["scale_in 20%"]),
                         ('360w', ["scale_in 40%"]),
                         ],
               'default': '1x',
             },
    }