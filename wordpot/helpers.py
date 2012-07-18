#!/usr/bin/env python

from flask import request
from wordpot import app
from wordpot.logger import LOGGER
import re

# --------------
# TimThumb check
# --------------

TIMTHUMB_RE     = re.compile('[tim]*thumb|uploadify', re.I)

def timthumb(subpath):
    """ Basic RE check to find timthumb related requests """
    if TIMTHUMB_RE.search(subpath) is not None:
        return True
    return False

# ----------------
# User enumeration
# ----------------

def user_enumeration(args):
    origin = request.remote_addr
    if 'author' in args:
        for k, a in enumerate(app.config['AUTHORS']):
            if (k + 1) == int(args['author']):
                print 'success'
                LOGGER.info('%s probed author page for: %s', origin, a)
                return True
    return False

# -----------------
# Plugins whitelist
# -----------------

def is_plugin_whitelisted(plugin):
    # If no whitelist has been set, return True
    if len(app.config['PLUGINS']) == 0:
        return True

    if plugin in app.config['PLUGINS']:
        return True

    return False

# ----------------
# Themes whitelist
# ----------------

def is_theme_whitelisted(theme):
    # If no whitelist has been set, return True
    if len(app.config['THEMES']) == 0:
        return True
    
    # If the theme probed is the theme in use
    if theme == app.config['THEME']:
        return True

    if theme in app.config['THEMES']:
        return True

    return False
