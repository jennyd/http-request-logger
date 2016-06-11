# HTTP request logger

This is a [Falcon](https://github.com/falconry/falcon) application which logs
all requests to `/logger` and returns `200`. It's intended for running on a local network
at a security workshop.

## Development

Make a virtualenv and install the dependencies:

```
mkvirtualenv -p /usr/bin/python3 http-request-logger
pip install -r requirements.txt
```

Run the app with gunicorn, reloading files when they change and logging to
stdout:

```
gunicorn --reload --access-logfile - --error-logfile - logger:app
```
