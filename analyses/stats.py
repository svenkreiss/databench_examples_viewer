"""Providing simple stats about the currently running instance."""


import databench


ANALYSIS = databench.Analysis('stats', __name__)
ANALYSIS.description = __doc__
ANALYSIS.show_in_index = False


@ANALYSIS.signals.on('connect')
def onconnect():
    """Run as soon as a browser connects to this."""
    ANALYSIS.signals.emit('log', {'action': 'done'})
