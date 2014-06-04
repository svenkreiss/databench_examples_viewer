"""Calculating \\(\\pi\\) the simple way."""

import math
from time import sleep
from random import random

import databench


simplepi = databench.Analysis('simplepi', __name__)
simplepi.description = __doc__
simplepi.thumbnail = 'simplepi.png'

@simplepi.signals.on('connect')
def onconnect():
    """Run as soon as a browser connects to this."""

    inside = 0
    for i in range(10000):
        sleep(0.001)
        r1 = random()
        r2 = random()
        if r1*r1 + r2*r2 < 1.0:
            inside += 1

        if (i+1)%100 == 0:
            draws = i+1
            simplepi.signals.emit('log', {'draws':draws, 'inside':inside})

            p = float(inside)/draws
            uncertainty = 4.0*math.sqrt(draws*p*(1.0 - p)) / draws
            simplepi.signals.emit('status', {
                'pi-estimate': 4.0*inside/draws,
                'pi-uncertainty': uncertainty
            })

    simplepi.signals.emit('log', {'action': 'done'})
