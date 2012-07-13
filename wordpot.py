#!/usr/bin/env python

try:
    from flask import Flask
except ImportError:
    print "\n[X] Please install Flask:"
    print "   $ pip install flask\n"
    exit()

from wordpot import app
from wordpot.logger import *
from optparse import OptionParser

def parse_options():
    usage = "usage: %prog [options]"

    parser = OptionParser(usage=usage)
    parser.add_option('--host', dest='host', default='127.0.0.1', help='Host address')
    parser.add_option('--port', dest='port', default='80', help='Port number')
    parser.add_option('--title', dest='title', default='Random Ramblings', help='Blog title')
    parser.add_option('--theme', dest='theme', default='twentyeleven', help='Default theme name')
    parser.add_option('--ver', dest='version', default='2.8', help='Wordpress version')

    (options, args) = parser.parse_args()
    
    app.config['HOST'] = options.host
    app.config['PORT'] = options.port
    app.config['BLOGTITLE'] = options.title
    app.config['THEME'] = options.theme
    app.config['VERSION'] = options.version

# Import config from file
app.config.from_pyfile('../wordpot.conf')

if __name__ == '__main__':
    parse_options()
    logging_setup()

    app.logger.info('Honeypot started on %s:%s', app.config['HOST'], app.config['PORT'])
    app.run(debug=app.debug, host=app.config['HOST'], port=int(app.config['PORT']))
    
