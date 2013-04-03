#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from utils import *
from blog import *


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        return render_str(template, **params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainHandler(Handler):
    def get(self):
       self.render('index.html')

class TimelineHandler(Handler):
    def get(self):
       self.render('timeline.html')

class WorksHandler(Handler):
    def get(self):
       self.render('works.html')



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/timelineCV', TimelineHandler),
    ('/works', WorksHandler),
   ('/blog/?', BlogFront),
   ('/blog/([0-9]+)', PostPage),
   ('/blog/newpost', NewPost)
], debug=True)
