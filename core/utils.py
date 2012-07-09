#!/usr/bin/env python

from werkzeug.routing import BaseConverter
import re


# ---------------
# Regex Converter
# ---------------

class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]

# --------------
# TimThumb check
# --------------

TIMTHUMB_RE     = re.compile('[tim]*thumb|uploadify', re.I)

def timthumb(subpath):
    """ Basic RE check to find timthumb related requests """
    if TIMTHUMB_RE.search(subpath) is not None:
        return True
    return False

