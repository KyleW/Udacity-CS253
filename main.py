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
import os
import webapp2
import jinja2
import rot13
import signup
import blogger
from google.appengine.ext import db

jinja_environment=jinja2.Environment(autoescape=True,loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'templates')))


class MainHandler(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('index.html')
		self.response.write(template.render())

class Resume(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('resume.html')
		self.response.write(template.render())
	
class Hello(webapp2.RequestHandler):
	def get(self):
		self.response.write("Hello, Udacity!")

app = webapp2.WSGIApplication([('/', MainHandler),
							('/resume',Resume),
							# unit 1
							('/hello',Hello),

							# unit1 2
							('/rot13',rot13.Rot13),

							# unit 3
							('/blog',blogger.Blog),
							('/newpost',blogger.NewPost),
							('/blog/newpost',blogger.NewPost),                               
							('/blog/([0-9]+)', blogger.PostPage),


							('/signup',signup.Signup),
							('/welcome',signup.Welcome)

							],
							 debug=True)
