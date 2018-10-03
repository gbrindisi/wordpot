from wordpot.plugins_manager import BasePlugin
import re

RECENTBACKUPS_RE     = re.compile('recent-backups|downloadfile', re.I)

class Plugin(BasePlugin):
    def run(self):
        # Logic
        if RECENTBACKUPS_RE.search(self.inputs['subpath']) is not None:
            # Message to log
            log = '%s probed for recent-backups: %s' % (self.inputs['request'].remote_addr, self.inputs['subpath'])
            self.outputs['log'] = log
            self.outputs['log_json'] = self.to_json_log(filename=self.inputs['subpath'], plugin='recent-backups')
            # Template to render
            self.outputs['template'] = 'recent-backups.html'

        return
