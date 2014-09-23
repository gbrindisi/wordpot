from wordpot.plugins_manager import BasePlugin

class Plugin(BasePlugin):
    def run(self):
        # Initialize template vars dict 
        self.outputs['template_vars'] = {} 

        # Common files:
        # Real File -> Template
        common = {
                'readme.html': 'readme.html',
                'xmlrpc.php' : 'xmlrpc.html'
                 }
        
        # Logic
        origin = self.inputs['request'].remote_addr
        if self.inputs['filename'] is not None and self.inputs['ext'] is not None:
            filename = self.inputs['filename'] + '.' + self.inputs['ext']

            if filename in common:
                self.outputs['log'] = '%s probed for: %s' % (origin, filename)
                self.outputs['log_json'] = self.to_json_log(filename=filename, plugin='commonfiles')
                self.outputs['template'] = common[filename]

        return
