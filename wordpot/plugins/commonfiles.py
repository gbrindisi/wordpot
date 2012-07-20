from wordpot.plugins_manager import BasePlugin

class Plugin(BasePlugin):
    def run(self, **kwargs):
        # Result dict to return
        res = {}
        res['template_vars'] = {}

        # Store input arguments
        args = self.parse_arguments(**kwargs)

        # Common files:
        # Real File -> Template
        common = {
                'readme.html': 'readme.html',
                'xmlrpc.php' : 'xmlrpc.html'
                 }

        # Logic
        origin = args['request'].remote_addr
        if args['file'] is not None and args['ext'] is not None:
            filename = args['file'] + '.' + args['ext']

            if filename in common:
                res['log'] = '%s probed for: %s' % (origin, filename)
                res['template'] = common[filename]

        return res
