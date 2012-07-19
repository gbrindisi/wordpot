#!/usr/bin/env python

try:
    from flask import Flask
except ImportError:
    print "\n[X] Please install Flask:"
    print "   $ pip install flask\n"
    exit()

from wordpot import app, pm 
from wordpot.logger import *
from optparse import OptionParser
import os

def parse_options():
    usage = "usage: %prog [options]"

    parser = OptionParser(usage=usage)
    parser.add_option('--host', dest='HOST', help='Host address')
    parser.add_option('--port', dest='PORT', help='Port number')
    parser.add_option('--title', dest='BLOGTITLE', help='Blog title')
    parser.add_option('--theme', dest='THEME', help='Default theme name')
    parser.add_option('--ver', dest='VERSION', help='Wordpress version')

    (options, args) = parser.parse_args()
    
    for opt, val in options.__dict__.iteritems():
        if val is not None:
            app.config[opt] = val

# Import config from file
conffile = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'wordpot.conf')
app.config.from_pyfile(conffile)

# Setup logging before execute the main
logging_setup()

if __name__ == '__main__':
    parse_options()

    LOGGER.info('Honeypot started on %s:%s', app.config['HOST'], app.config['PORT'])
    app.run(debug=app.debug, host=app.config['HOST'], port=int(app.config['PORT']))
    
