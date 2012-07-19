from wordpot.plugins_manager import BasePlugin
import re

TIMTHUMB_RE     = re.compile('[tim]*thumb|uploadify', re.I)

class Plugin(BasePlugin):
    def run(self, **kwargs):
        # Result dict to return
        res = {}
        
        # Store input arguments
        args = {}
        for k, v in kwargs.iteritems():
            args[k] = v

        # Logic
        if TIMTHUMB_RE.search(args['subpath']) is not None:
            # Message to log
            log = '%s probed for timthumb: %s' % (args['request'].remote_addr, args['subpath'])
            res['log'] = log

            # Template to render
            res['template'] = 'timthumb.html'

        return res
