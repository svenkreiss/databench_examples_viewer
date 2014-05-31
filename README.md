# Databench Examples Viewer

> Shows some of the examples for [Databench](https://github.com/svenkreiss/databench) from [databench_examples](https://github.com/svenkreiss/databench_examples) on a Heroku instance.


# Reducing compile time with special buildpack

```bash
heroku config:set BUILDPACK_URL=https://github.com/dbrgn/heroku-buildpack-python-sklearn/
```

Which needs these exact versions:

```
argparse==1.2.1
distribute==0.6.24
gunicorn==17.5
wsgiref==0.1.2
numpy==1.7.0
matplotlib==1.1.0
scipy==0.11.0
scikit-learn==0.13.1
```


# Port

Databench will pick up the environment variable `PORT`. This functionally was introduced in Databench 0.1.1.

Starting version 0.1.2, databench responds to non-local requests.
