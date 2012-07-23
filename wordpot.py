#!/usr/bin/env python

try:
    from flask import Flask
except ImportError:
    print "\n[X] Please install Flask:"
    print "   $ pip install flask\n"
    exit()

from wordpot import app, pm, parse_options, check_options 
from wordpot.logger import *
import os

check_options()

if __name__ == '__main__':
    parse_options()
    LOGGER.info('Checking command line options')
    check_options()

    LOGGER.info('Honeypot started on %s:%s', app.config['HOST'], app.config['PORT'])
    app.run(debug=app.debug, host=app.config['HOST'], port=int(app.config['PORT']))
    
