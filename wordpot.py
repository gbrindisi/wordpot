#/usr/bin/env python

try:
    from flask import Flask, request, render_template
except ImportError:
    print "\n[X] Please install Flask:"
    print "   $ pip install flask\n"
    exit()

from optparse import OptionParser
from core.utils import RegexConverter, timthumb
import logging

app = Flask(__name__)
app.url_map.converters['regex'] = RegexConverter

# -------
# Globals
# -------

HOST            = ''
PORT            = ''
BLOGTITLE       = ''
VERSION         = ''
LOGGER          = logging.getLogger('wordpot')

# -------
# Logging
# -------

def logging_setup():
    # File handler
    fh = logging.FileHandler('wordpot.log')
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    fh.setFormatter(formatter)

    # Add handlers
    LOGGER.addHandler(fh)
   
    # Set level
    LOGGER.setLevel(logging.INFO)
    
    return True

# ------
# Routes
# ------

@app.route('/')
def homepage(file=None, path=None, subpath=None):
    return render_template('dummy.html', blogtitle=BLOGTITLE, version=VERSION)

@app.route('/readme.html', methods=['GET', 'POST'])
def readme():
    """ Readme probing handler """
    origin = request.remote_addr
    LOGGER.info('%s probed for the readme', origin)
    return render_template('readme.html', version=VERSION)

@app.route('/wp-admin<regex("\/.*"):subpath>', methods=['GET', 'POST'])
def admin(subpath):
    """ Admin panel probing handler """
    origin = request.remote_addr
    LOGGER.info('%s probed for the admin panel with path: %s', origin, subpath)
    return render_template('wp-login.html', blogtitle=BLOGTITLE, version=VERSION)

@app.route('/wp-content/plugins/<plugin>', methods=['GET', 'POST'])
@app.route('/wp-content/plugins/<plugin><regex("(\/.*)"):subpath>', methods=['GET', 'POST'])
def plugin(plugin, subpath='/'):
    """ Plugin probing handler """
    origin = request.remote_addr
    LOGGER.info('%s probed a plugin: "%s" with path "%s"', origin, plugin, subpath)
    if timthumb(subpath):
        LOGGER.info('%s probed for timthumb: %s', origin, subpath)
    return render_template('dummy.html', blogtitle=BLOGTITLE, version=VERSION)

@app.route('/wp-content/themes/<plugin>', methods=['GET', 'POST'])
@app.route('/wp-content/themes/<theme><regex("(\/.*)"):subpath>', methods=['GET', 'POST'])
def theme(theme, subpath='/'):
    """ Theme probing handler """
    origin = request.remote_addr
    LOGGER.info('%s probed a theme: "%s" with path "%s"', origin, theme, subpath)
    if timthumb(subpath):
        LOGGER.info('%s probed for timthumb: %s', origin, subpath)
    return render_template('dummy.html', blogtitle=BLOGTITLE, version=VERSION) 

# -------------
# Option parser
# -------------

def parse_options():
    usage = "usage: %prog [options]"

    parser = OptionParser(usage=usage)
    parser.add_option('--host', dest='host', default='127.0.0.1', help='Host address')
    parser.add_option('--port', dest='port', default='80', help='Port number')
    parser.add_option('--title', dest='title', default='Random Rambling', help='Blog title')
    parser.add_option('--ver', dest='version', default='2.8', help='Wordpress version')

    (options, args) = parser.parse_args()

    # Ugly!
    global HOST  
    global PORT      
    global BLOGTITLE    
    global VERSION 

    HOST         = options.host
    PORT         = options.port
    BLOGTITLE    = options.title
    VERSION      = options.version

    return True

if __name__ == '__main__':
    logging_setup() 
    parse_options()

    LOGGER.info('Honeypot started.')
    app.run(host=HOST, port=int(PORT))
