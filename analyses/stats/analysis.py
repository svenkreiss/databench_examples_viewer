"""Providing simple stats about the currently running instance."""

import databench


class Analysis(databench.Analysis):
    def on_connect(self):
        """Run as soon as a browser connects to this."""
        self.emit('log', {'action': 'done'})


META = databench.Meta('stats', __name__, __doc__, Analysis)
META.show_in_index = False
