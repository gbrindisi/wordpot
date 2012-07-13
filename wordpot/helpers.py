#!/usr/bin/env python

from flask import request
from wordpot import app
import re
from wordpot.logger import *

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
