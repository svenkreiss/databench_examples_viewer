# Databench Examples Viewer

> Shows some of the examples for [Databench](https://github.com/svenkreiss/databench) from [databench_examples](https://github.com/svenkreiss/databench_examples) on a Heroku instance.


# Reducing compile time with special buildpack

Using this buildpack: https://github.com/thenovices/heroku-buildpack-scipy

```bash
heroku config:set BUILDPACK_URL=https://github.com/thenovices/heroku-buildpack-scipy
```

Which needs these exact versions:

```
numpy==1.8.1
scipy==0.14.0
```


# Port

Databench will pick up the environment variable `PORT`. This functionally was introduced in Databench 0.1.1.
