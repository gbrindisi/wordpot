from wordpot.plugins_manager import BasePlugin

class Plugin(BasePlugin):
    def run(self):
        # Initialize template vars dict 
        self.outputs['template_vars'] = {} 

        # First check if the file is wp-login.php
        if not (self.inputs['filename'] == 'wp-login' and self.inputs['ext'] == 'php'):
            return 

        # Logic
        origin = self.inputs['request'].remote_addr

        if self.inputs['request'].method == 'POST':
            username = self.inputs['request'].form['log']
            password = self.inputs['request'].form['pwd']
            self.outputs['log'] = '%s tried to login with username %s and password %s' % (origin, username, password)
            self.outputs['log_json'] = self.to_json_log(username=username, password=password, plugin='badlogin')
            self.outputs['template_vars']['BADLOGIN'] = True
            self.outputs['template'] = 'wp-login.html'
        else:
            self.outputs['log'] = '%s probed for the login page' % origin
            self.outputs['template_vars']['BADLOGIN'] = False 
            self.outputs['template'] = 'wp-login.html'

        return
