from wordpot.plugins_manager import BasePlugin

class Plugin(BasePlugin):
    def run(self, **kwargs):
        # Result dict to return
        res = {}
        res['template_vars'] = {}
        res['template'] = 'wp-login.html'

        # Store input arguments
        args = self.parse_arguments(**kwargs)

        # First check if the file is wp-login.php
        if not (args['file'] == 'wp-login' and args['ext'] == 'php'):
            return {}

        # Logic
        origin = args['request'].remote_addr

        if args['request'].method == 'POST':
            username = args['request'].form['log']
            password = args['request'].form['pwd']
            res['log'] = '%s tried to login with username %s and password %s' % (origin, username, password)
            res['template_vars']['BADLOGIN'] = True
        else:
            res['log'] = '%s probed for the login page' % origin
            res['template_vars']['BADLOGIN'] = False

        return res
