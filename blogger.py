import os
import webapp2
import jinja2

jinja_environment=jinja2.Environment(autoescape=True,loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'templates')))


class Blog(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('blog.html')
		self.response.write(template.render())

class NewPost(webapp2.RequestHandler):
	def get(self):
		self.response.write("Time to write a new blog post.")

