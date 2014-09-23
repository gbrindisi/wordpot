from wordpot.plugins_manager import BasePlugin
from wordpot import app

class Plugin(BasePlugin):
    def run(self):
        # Initialize template vars dict 
        self.outputs['template_vars'] = {} 

        # Logic
        origin = self.inputs['request'].remote_addr
        req_args = self.inputs['request'].args 

        if 'author' in req_args:
            for k, a in enumerate(app.config['AUTHORS']):
                if (k + 1) == int(req_args['author']):
                    self.outputs['log'] = '%s probed author page for user: %s' % (origin, a)
                    self.outputs['log_json'] = self.to_json_log(author=a, plugin='userenumeration')
                    self.outputs['template_vars']['AUTHORPAGE'] = True
                    self.outputs['template_vars']['CURRENTAUTHOR'] = (k+1, a)
                    self.outputs['template'] = app.config['THEME'] + '.html'

        return 
