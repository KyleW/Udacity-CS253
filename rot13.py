import os
import webapp2
import jinja2

jinja_environment=jinja2.Environment(autoescape=True,loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'templates')))


alphaNum = {
	"a":1,
	"b":2,
	"c":3,
	"d":4,
	"e":5,
	"f":6,
	"g":7,
	"h":8,
	"i":9,
	"j":10,
	"k":11,
	"l":12,
	"m":13,
	"n":14,
	"o":15,
	"p":16,
	"q":17,
	"r":18,
	"s":19,
	"t":20,
	"u":21,
	"v":22,
	"w":23,
	"x":24,
	"y":25,
	"z":26
}

numAlpha = {
	1:"a",
	2:"b",
	3:"c",
	4:"d",
	5:"e",
	6:"f",
	7:"g",
	8:"h",
	9:"i",
	10:"j",
	11:"k",
	12:"l",
	13:"m",
	14:"n",
	15:"o",
	16:"p",
	17:"q",
	18:"r",
	19:"s",
	20:"t",
	21:"u",
	22:"v",
	23:"w",
	24:"x",
	25:"y",
	26:"z"
}


# rot13 function
def rot13(str):
	# reset list
	holder=[]
	answer=""
	for c in str:
		if c.isalpha():
			# if yes, continue
			# store the case
			lowerCase= c.islower()

			# translate the letter into a number, add 13, mod 26
			val=(alphaNum[c.lower()]+13) % 26

			# Cover 'z' case
			if val==0:
				val=26

			# lookup the new letter
			new=numAlpha[val]

			# add to list
			if lowerCase:
				holder.append(new)
			else:
				holder.append(new.upper())
		else :
			# if no, add to list as is
			holder.append(c)
	# turn list into string
	answer = ''.join(holder)
	# return answer
	return answer


class Rot13(webapp2.RequestHandler):
	def write_form (self,last="",rot13="", error=""):
		error_message=self.error
		template = jinja_environment.get_template('rot13.html')
		template_values = {
			'last':last,
			'error': error,
			'rot13':rot13
        }

		self.response.write(template.render(template_values))

	def get(self):
		self.write_form()

	def post(self):
		q= self.request.get("text")
		final_val= rot13(q)
		self.write_form(last=q,rot13=final_val,error="That doesn't look valid to me friend")