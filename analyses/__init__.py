"""Databench is a tool that connects a Python analysis to a custom html frontend.
It provides various handy tools like `markdown` and `MathJax` to mark up the 
frontend. It also includes a connector from `matplotlib` to `d3.js` using 
`mpld3`. It even allows for the frontend to make use of `angular.js`. Below 
are simple live demos. Some more advanced examples like asynchonously
subscribing to a Redis channel and parallel processing with Redis Queue cannot
be shown here but are available in the 
[github/databench_examples](https://github.com/svenkreiss/databench_examples)
repository.

Main GitHub page: [github/databench](https://github.com/svenkreiss/databench)  
Advanced examples: 
[github/databench_examples](https://github.com/svenkreiss/databench_examples)  
User guide and API: 
[svenkreiss.com/databench/](http://www.svenkreiss.com/databench/)"""

import analyses.simplepi
# import analyses.slowpi
import analyses.mpld3pi
import analyses.mpld3PointLabel
import analyses.mpld3Drag
import analyses.bagofchars
import analyses.bagofcharsd3
import analyses.angular
