import os
import webapp2
import jinja2
import re

jinja_environment=jinja2.Environment(autoescape=True,loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'templates')))

# Name, password and password are present
# Passwords match
# Email address is properly formatted


USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
	return USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
	return PASS_RE.match(password)

EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
def valid_email(email):
	return EMAIL_RE.match(email)

class Signup(webapp2.RequestHandler):
	def write_form (self,name="",email="",errorN="",errorP="",errorV="",errorE=""):
		template = jinja_environment.get_template('signup.html')
		template_values = {
			'name':name,
			'email': email,
			'errorN':errorN,
			'errorP':errorP,
			'errorV':errorV,
			'errorE':errorE
        }
		self.response.write(template.render(template_values))
	
	def get(self):
		name=self.request.get("name")
		email=self.request.get("email")
		self.write_form(name=name,email=email) 

	def post(self):
		error=0
		errorN=""
		errorP=""
		errorV=""
		errorE=""


		name=self.request.get("username")
		password=self.request.get("password")
		verify=self.request.get("verify")
		email=self.request.get("email")

		#check username
		if name:
			if valid_username(name):
				pass
			else:
				errorN="Invalid Username"
				error+=1	
		else:
			errorN="Invalid Username"
			error+=1

		#check password
		if password:
			if valid_password(password):
				pass
			else:
				errorP="Invalid Password"
				error+=1
		else:
			errorP="Invalid Password"
			error+=1

		#check verify password
		if verify:
			if password == verify:
				pass
			else:
				errorV="Try Again"
				error+=1
		else:
			errorV="Try Again"
			error+=1

		#check email
		if email:
			if valid_email(email):
				pass
			else:
				errorE="Invalid Email"
				error +=1
		else:
			pass

		#if valid redirect to welcome
		if error==0:
			self.redirect("/welcome?username="+name)
		else:
			self.write_form(name=name,email=email,errorN=errorN,errorP=errorP,errorV=errorV,errorE=errorE) 		

class Welcome(webapp2.RequestHandler):
	def get(self):
		self.response.write("Welcome, "+self.request.get("username")+"!")