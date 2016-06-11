#!/usr/bin/env python3

import falcon
import datetime
import os


class RequestLogger(object):
    """Log all requests.
    """

    def format_request(self, req):
        """Construct a bytes object similar to the original HTTP request.

        This won't be exactly the same as the original request, because the
        header names have been modified on their way through gunicorn (PEP 3333
        specifies that most headers are passed to the application as HTTP_ keys
        in the environ dict). The header names will be upper-cased, and the
        headers also may have been reordered.
        """
        env = req.env
        r = '{} {} {}\n'.format(req.method, req.relative_uri, env['SERVER_PROTOCOL'])
        for header, value in req.headers.items():
            r += '{}: {}\n'.format(header, value)
        r += '\n'
        encoded = r.encode()
        encoded += req.stream.read()

        return encoded

    def log_request(self, req):
        """Save the formatted request to a file in saved_requests.
        """
        dirname = 'saved_requests'
        filename = datetime.datetime.utcnow().isoformat().replace(':', '-')
        path = os.path.join(dirname, filename)

        formatted_request = self.format_request(req)
        with open(path, 'wb') as f:
            f.write(formatted_request)

    def response(self, resp):
        """Construct a standard 200 text response to use for all methods.
        """
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/plain; charset=UTF-8'
        resp.body = ('request logged')

    def log_and_respond(self, req, resp):
        self.log_request(req)
        self.response(resp)

    def on_head(self, req, resp):
        self.log_and_respond(req, resp)

    def on_get(self, req, resp):
        self.log_and_respond(req, resp)

    def on_post(self, req, resp):
        self.log_and_respond(req, resp)

    def on_put(self, req, resp):
        self.log_and_respond(req, resp)

    def on_patch(self, req, resp):
        self.log_and_respond(req, resp)

    def on_delete(self, req, resp):
        self.log_and_respond(req, resp)

    def on_options(self, req, resp):
        self.log_and_respond(req, resp)

    def on_trace(self, req, resp):
        self.log_and_respond(req, resp)

    def on_connect(self, req, resp):
        self.log_and_respond(req, resp)


app = falcon.API()

request_logger = RequestLogger()

app.add_route('/logger', request_logger)
