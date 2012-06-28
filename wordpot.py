from flask import Flask, request, render_template
from werkzeug.routing import BaseConverter
import re
import logging

app = Flask(__name__)

TIMTHUMB_RE     = re.compile('[tim]*thumb|uploadify', re.I)
HOST            = '127.0.0.1'
PORT            = '5000'
BLOGTITLE       = 'Random Ramblings'
VERSION         = '2.8'


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]

app.url_map.converters['regex'] = RegexConverter

def logging_setup():
    fh = logging.FileHandler('wordpot.log')
    fh.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    fh.setFormatter(formatter)
    app.logger.addHandler(fh)


def timthumb(subpath):
    """ Basic RE check to find timthumb related requests """
    if TIMTHUMB_RE.search(subpath) is not None:
        return True
    return False

@app.route('/')
def homepage(file=None, path=None, subpath=None):
    return render_template('dummy.html', blogtitle=BLOGTITLE, version=VERSION)

@app.route('/readme.html', methods=['GET', 'POST'])
def readme():
    """ Readme probing handler """
    origin = request.remote_addr
    app.logger.info('%s probed for the readme', origin)
    return render_template('readme.html', version=VERSION)

@app.route('/wp-admin<regex("\/.*"):subpath>', methods=['GET', 'POST'])
def admin(subpath):
    """ Admin panel probing handler """
    origin = request.remote_addr
    app.logger.info('%s probed for the admin panel with path: %s', origin, subpath)
    return render_template('wp-login.html', blogtitle=BLOGTITLE, version=VERSION)

@app.route('/wp-content/plugins/<plugin><regex("\/.*"):subpath>', methods=['GET', 'POST'])
def plugin(plugin, subpath):
    """ Plugin probing handler """
    origin = request.remote_addr
    app.logger.info('%s probed a plugin: %s', origin, plugin)
    if timthumb(subpath):
        app.logger.info('%s probed for timthumb: %s', origin, subpath)
    return render_template('dummy.html', blogtitle=BLOGTITLE, version=VERSION)

@app.route('/wp-content/themes/<theme><regex("\/.*"):subpath>', methods=['GET', 'POST'])
def theme(theme, subpath):
    """ Theme probing handler """
    origin = request.remote_addr
    app.logger.info('%s probed a theme: %s', origin, theme)
    if timthumb(subpath):
        app.logger.info('%s probed for timthumb: %s', origin, subpath)
    return render_template('dummy.html', blogtitle=BLOGTITLE, version=VERSION) 

if __name__ == '__main__':
    logging_setup()
    app.run(debug=True, host=HOST, port=int(PORT))
