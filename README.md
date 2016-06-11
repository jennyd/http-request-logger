# HTTP request logger

This is a [Falcon](https://github.com/falconry/falcon) application which accepts
all requests made to `/logger`, saves the request to a file and returns `200`.
It's intended for running on a local network at a security workshop.

Requests are written in the `saved_requests` directory as individual files, as
similarly to the original raw requests as I could make them after they've been
through a WSGI server.

## Development

Make a virtualenv and install the dependencies:

```
mkvirtualenv -p /usr/bin/python3 http-request-logger
pip install -r requirements.txt
```

Run the app with gunicorn, reloading files when they change and logging to
stdout:

```
gunicorn -c gunicorn_config_development logger:app
```
