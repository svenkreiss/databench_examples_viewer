"""Databench is a tool that connects a Python analysis to a custom html
frontend. It provides various handy tools like `markdown` and `MathJax` to
mark up the frontend. It also includes a connector from `matplotlib` to
`d3.js` using `mpld3`. It even allows for the frontend to make use of
`angular.js`. Below are simple live demos. Some more advanced examples
like asynchonously subscribing to a Redis channel and parallel processing
with Redis Queue cannot be shown here but are available in the GitHub
repository
[svenkreiss/databench_examples](https://github.com/svenkreiss/databench_examples).

User guide and API:
[databench.trivial.io/v0.3/](http://databench.trivial.io/v0.3/)
"""

__version__ = "0.2.1"

header_title = 'Databench Online Examples'


import bagofcharsd3.analysis
import flowers.analysis
# import mpld3Drag.analysis
# import mpld3PointLabel.analysis
# import mpld3pi.analysis
import angular.analysis
import simplepi.analysis

import stats.analysis
