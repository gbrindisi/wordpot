from wordpot.plugins_manager import BasePlugin
import re

TIMTHUMB_RE     = re.compile('[tim]*thumb|uploadify', re.I)

class Plugin(BasePlugin):
    def run(self):
        # Logic
        if TIMTHUMB_RE.search(self.inputs['subpath']) is not None:
            # Message to log
            log = '%s probed for timthumb: %s' % (self.inputs['request'].remote_addr, self.inputs['subpath'])
            self.outputs['log'] = log

            # Template to render
            self.outputs['template'] = 'timthumb.html'

        return
