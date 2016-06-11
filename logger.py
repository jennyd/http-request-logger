#!/usr/bin/env python3

import falcon


class RequestLogger(object):
    """Log all requests.
    """

    def log_request(self, req):
        pass

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
