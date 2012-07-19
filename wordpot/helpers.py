#!/usr/bin/env python

from flask import request
from wordpot import app
from wordpot.logger import LOGGER

# -----------------
# Plugins whitelist
# -----------------

def is_plugin_whitelisted(plugin):
    # If PLUGINS option doesn't exist allow all
    if 'PLUGINS' not in app.config:
        return True
    else:
        # Plugin is in the whitelist
        if plugin in app.config['PLUGINS']:
            return True
    return False

# ----------------
# Themes whitelist
# ----------------

def is_theme_whitelisted(theme):
    # If THEMES options doesn't exist allow all  
    if 'THEMES' not in app.config:
        return True
    else:
        # Theme is in the whitelist
        if theme in app.config['THEMES'] or theme == app.config['THEME']:
            return True
    return False
