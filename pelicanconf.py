#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'ramz'
SITENAME = u'My Life "My Code"'
SITEURL = 'http://localhost:8000'

THEME = 'pelican-themes/elegant'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)
LINKS = ()

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

SOCIAL = ()

DEFAULT_PAGINATION = 20
RECENT_ARTICLES_COUNT = 20

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
PLUGIN_PATHS=["pelican-plugins"]
PLUGINS = ['pelican_gist'
           # ,'liquid_tags.img', 'liquid_tags.video',
           # 'liquid_tags.youtube', 'liquid_tags.vimeo','liquid_tags.include_code', 'ipynb'
       ]
