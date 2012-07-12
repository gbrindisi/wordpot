#/usr/bin/env python

try:
    from flask import Flask, request, render_template, make_response, url_for, redirect
except ImportError:
    print "\n[X] Please install Flask:"
    print "   $ pip install flask\n"
    exit()

from optparse import OptionParser
from core.utils import RegexConverter, timthumb
import logging

# /*, static_url_path='/wp-content'
app = Flask(__name__)
app.url_map.converters['regex'] = RegexConverter

# -------
# Globals
# -------

HOST            = ''
PORT            = ''
LOGGER          = logging.getLogger('wordpot')
TEMPLATE_VARS   = {
        'BLOGTITLE': '',
        'VERSION':   '',
        'THEME':     '',
        'AUTHOR':    ''
                  }

# Just admin for now, planning to extend this in the future
AUTHORS         = []
AUTHORS.append( {'id': '1', 'username': 'admin'} )
TEMPLATE_VARS['AUTHOR'] = AUTHORS[0]

ERRORS          = {}


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

# -------
# Helpers
# -------

def user_enumeration(args):
    if 'author' in args:
        global TEMPLATE_VARS
        for author in AUTHORS:
            if author['id'] == args['author']:
                TEMPLATE_VARS['AUTHOR'] = author
                return True
    return False

# ------
# Routes
# ------

@app.route('/')
@app.route('/index.php')
def homepage():
    origin = request.remote_addr
    if user_enumeration(request.args):
        author =  TEMPLATE_VARS['AUTHOR']['username']
        LOGGER.info('%s probed author page for: %s', origin, author)
        return render_template('dummy.html', tpl=TEMPLATE_VARS, pagetype='authorarchive')
    else:
        return render_template('dummy.html', tpl=TEMPLATE_VARS)

@app.route('/readme.html', methods=['GET', 'POST'])
def readme():
    """ Readme probing handler """
    origin = request.remote_addr
    LOGGER.info('%s probed for the readme', origin)
    return render_template('readme.html', tpl=TEMPLATE_VARS)

@app.route('/xmlrpc.php', methods=['GET', 'POST'])
def xmlrpc():
    """ xmlrpc.php probing handler """
    origin = request.remote_addr
    LOGGER.info('%s probed for xmlrpc.php', origin)
    return render_template('xmlrpc.html') 

@app.route('/wp-login.php', methods=['GET', 'POST'])
def login():
    origin = request.remote_addr
    if request.method == 'POST':
        username = request.form['log']
        password = request.form['pwd']
        LOGGER.info('%s tried to login with username %s and password %s', origin, username, password)
        ERRORS['BADLOGIN'] = True
        return render_template('wp-login.html', tpl=TEMPLATE_VARS, errors=ERRORS)
    else:
        ERRORS['BADLOGIN'] = False
        LOGGER.info('%s probed for the login page', origin)
        return render_template('wp-login.html', tpl=TEMPLATE_VARS, errors=ERRORS)

@app.route('/wp-admin<regex("\/.*"):subpath>', methods=['GET', 'POST'])
def admin(subpath='/'):
    """ Admin panel probing handler """
    origin = request.remote_addr
    LOGGER.info('%s probed for the admin panel with path: %s', origin, subpath)
    return redirect(url_for('login'))

@app.route('/wp-content/plugins/<plugin>', methods=['GET', 'POST'])
@app.route('/wp-content/plugins/<plugin><regex("(\/.*)"):subpath>', methods=['GET', 'POST'])
def plugin(plugin, subpath='/'):
    """ Plugin probing handler """
    origin = request.remote_addr
    LOGGER.info('%s probed a plugin: "%s" with path "%s"', origin, plugin, subpath)
    if timthumb(subpath):
        LOGGER.info('%s probed for timthumb: %s', origin, subpath)
        return render_template('timthumb.html') 
    return render_template('dummy.html', tpl=TEMPLATE_VARS)

@app.route('/wp-content/themes/<theme>', methods=['GET', 'POST'])
@app.route('/wp-content/themes/<theme><regex("(\/.*)"):subpath>', methods=['GET', 'POST'])
def theme(theme, subpath='/'):
    """ Theme probing handler """
    origin = request.remote_addr
    LOGGER.info('%s probed a theme: "%s" with path "%s"', origin, theme, subpath)
    if timthumb(subpath):
        LOGGER.info('%s probed for timthumb: %s', origin, subpath)
        return render_template('timthumb.html')
    return render_template('dummy.html', tpl=TEMPLATE_VARS) 

# -------------
# Option parser
# -------------

def parse_options():
    usage = "usage: %prog [options]"

    parser = OptionParser(usage=usage)
    parser.add_option('--host', dest='host', default='127.0.0.1', help='Host address')
    parser.add_option('--port', dest='port', default='80', help='Port number')
    parser.add_option('--title', dest='title', default='Random Ramblings', help='Blog title')
    parser.add_option('--theme', dest='theme', default='twentyeleven', help='Default theme name')
    parser.add_option('--ver', dest='version', default='2.8', help='Wordpress version')

    (options, args) = parser.parse_args()

    # Ugly!
    global HOST  
    global PORT      
    global TEMPLATE_VARS
    global BLOGTITLE   
    global THEME
    global VERSION

    HOST                        = options.host
    PORT                        = options.port
    TEMPLATE_VARS['BLOGTITLE']  = options.title
    TEMPLATE_VARS['THEME']      = options.theme
    TEMPLATE_VARS['VERSION']    = options.version

    return True

if __name__ == '__main__':
    logging_setup() 
    parse_options()

    LOGGER.info('Honeypot started.')
    app.run(host=HOST, port=int(PORT))
