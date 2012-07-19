from wordpot.plugins_manager import BasePlugin
from wordpot import app

class Plugin(BasePlugin):
    def run(self, **kwargs):
        # Result dict to return
        res = {}
        res['template_vars'] = {} 

        # Store input arguments
        args = {}
        for k, v in kwargs.iteritems():
            args[k] = v

        # Logic
        origin = args['request'].remote_addr
        req_args = args['request'].args 

        if 'author' in req_args:
            for k, a in enumerate(app.config['AUTHORS']):
                if (k + 1) == int(req_args['author']):
                    res['log'] = '%s probed author page for user: %s' % (origin, a)
                    res['template_vars']['AUTHORPAGE'] = True
                    res['template_vars']['CURRENTAUTHOR'] = (k+1, a)
                    res['template'] = 'dummy.html'

        return res
