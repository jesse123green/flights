import webapp2
from webapp2_extras import jinja2
from google.appengine.api import urlfetch
import logging,datetime
import urllib
import urllib2
import json,os



class BaseHandler(webapp2.RequestHandler):

    @webapp2.cached_property
    def jinja2(self):
        # Returns a Jinja2 renderer cached in the app registry.
        return jinja2.get_jinja2(app=self.app)

    def render_response(self, _template, **context):
        # Renders a template and writes the result to the response.
        rv = self.jinja2.render_template(_template, **context)
        self.response.write(rv)


class IndexHandler(BaseHandler):

    def get(self):
        context = {'placeholder':'get'}
        self.render_response('index.html', **context)

    def post(self):
        context = {'placeholder':'post'}
        self.render_response('index.html',**context)
