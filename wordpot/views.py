#!/usr/bin/env python

from flask import request, render_template, redirect, url_for, abort
from wordpot import app, pm
from wordpot.helpers import *
from wordpot.logger import LOGGER

@app.route('/', methods=['GET', 'POST'])
@app.route('/<file>.<ext>', methods=['GET', 'POST'])
def commons(file=None, ext=None):

    # Plugins hook
    for p in pm.hook('commons'):
        try:
            res = p.run(file=file, ext=ext, request=request)
            if 'log' in res:
                LOGGER.info(res['log'])
            if 'template' in res:
                if 'template_vars' in res:
                    return render_template(res['template'], vars=res['template_vars'])
                return render_template(res['template'], vars={})
        except Exception, e:
            LOGGER.error('Unable to run plugin: %s\n%s', p.name, e.message)
   
    if file is None and ext is None:
        return render_template('dummy.html', vars={})
    elif file == 'index' and ext == 'php':
        return render_template('dummy.html', vars={})
    else:        
        abort(404)

@app.route('/wp-admin', methods=['GET', 'POST'])
@app.route('/wp-admin<regex("\/.*"):subpath>', methods=['GET', 'POST'])
def admin(subpath='/'):
    """ Admin panel probing handler """
    origin = request.remote_addr
    LOGGER.info('%s probed for the admin panel with path: %s', origin, subpath)
    
    # Plugins hook
    for p in pm.hook('plugins'):
        try:
            res = p.run(subpath=subpath, request=request)
            if 'log' in res:
                LOGGER.info(res['log'])
            if 'template' in res:
                if 'template_vars' in res:
                    return render_template(res['template'], vars=res['template_vars'])
                return render_template(res['template'], vars={})
        except Exception, e:
            LOGGER.error('Unable to run plugin: %s\n%s', p.name, e.message)
    
    return redirect('wp-login.php')

@app.route('/wp-content/plugins/<plugin>', methods=['GET', 'POST'])
@app.route('/wp-content/plugins/<plugin><regex("(\/.*)"):subpath>', methods=['GET', 'POST'])
def plugin(plugin, subpath='/'):
    """ Plugin probing handler """
    origin = request.remote_addr
    LOGGER.info('%s probed for plugin "%s" with path: %s', origin, plugin, subpath)
    
    # Is the plugin in the whitelist?
    if not is_plugin_whitelisted(plugin):
        abort(404)

    # Plugins hook
    for p in pm.hook('plugins'):
        try:
            res = p.run(plugin=plugin, subpath=subpath, request=request)
            if 'log' in res:
                LOGGER.info(res['log'])
            if 'template' in res:
                if 'template_vars' in res:
                    return render_template(res['template'], vars=res['template_vars'])
                return render_template(res['template'], vars={})
        except Exception, e:
            LOGGER.error('Unable to run plugin: %s\n%s', p.name, e.message)

    return render_template('dummy.html', vars={})

@app.route('/wp-content/themes/<theme>', methods=['GET', 'POST'])
@app.route('/wp-content/themes/<theme><regex("(\/.*)"):subpath>', methods=['GET', 'POST'])
def theme(theme, subpath='/'):
    """ Theme probing handler """
    origin = request.remote_addr
    LOGGER.info('%s probed for theme "%s" with path: %s', origin, theme, subpath)

    # Is the theme whitelisted?
    if not is_theme_whitelisted(theme):
        abort(404)

    # Plugins hook
    for p in pm.hook('themes'):
        try:
            res = p.run(theme=theme, subpath=subpath, request=request)
            if 'log' in res:
                LOGGER.info(res['log'])
            if 'template' in res:
                if 'template_vars' in res:
                    return render_template(res['template'], vars=res['template_vars'])
                return render_template(res['template'], vars={})
        except Exception, e:
            LOGGER.error('Unable to run plugin: %s\n%s', p.name, e.message)

    return render_template('dummy.html', vars={}) 

