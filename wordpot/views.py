#!/usr/bin/env python

from flask import request, render_template, redirect, url_for
from wordpot import app
from wordpot.helpers import *
from wordpot.logger import LOGGER

@app.route('/')
@app.route('/index.php')
def homepage():
    origin = request.remote_addr
    if user_enumeration(request.args):
        return render_template('dummy.html', pagetype='authorarchive')
    else:
        return render_template('dummy.html')

@app.route('/readme.html', methods=['GET', 'POST'])
def readme():
    """ Readme probing handler """
    origin = request.remote_addr
    LOGGER.info('%s probed for the readme', origin)
    return render_template('readme.html')

@app.route('/xmlrpc.php', methods=['GET', 'POST'])
def xmlrpc():
    """ xmlrpc.php probing handler """
    origin = request.remote_addr
    LOGGER.info('%s probed for xmlrpc.php', origin)
    return render_template('xmlrpc.html') 

@app.route('/wp-login.php', methods=['GET', 'POST'])
def login():
    """ Login page probing handler """
    origin = request.remote_addr
    ERRORS = {}
    if request.method == 'POST':
        username = request.form['log']
        password = request.form['pwd']
        LOGGER.info('%s tried to login with username %s and password %s', origin, username, password)
        ERRORS['BADLOGIN'] = True
        return render_template('wp-login.html', errors=ERRORS)
    else:
        ERRORS['BADLOGIN'] = False
        LOGGER.info('%s probed for the login page', origin)
        return render_template('wp-login.html', errors=ERRORS)

@app.route('/wp-admin', methods=['GET', 'POST'])
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
    return render_template('dummy.html')

@app.route('/wp-content/themes/<theme>', methods=['GET', 'POST'])
@app.route('/wp-content/themes/<theme><regex("(\/.*)"):subpath>', methods=['GET', 'POST'])
def theme(theme, subpath='/'):
    """ Theme probing handler """
    origin = request.remote_addr
    LOGGER.info('%s probed a theme: "%s" with path "%s"', origin, theme, subpath)
    if timthumb(subpath):
        LOGGER.info('%s probed for timthumb: %s', origin, subpath)
        return render_template('timthumb.html')
    return render_template('dummy.html') 

