from flask import Flask,render_template,request
from jinja2 import Template


# this makes app an instance of the Flask class
# and it passed the special variable __name__ into
# the constructor
 


app = Flask(__name__)

@app.route("/")
def index():
	name = request.args.get("name",None)
	email = request.args.get("email",None)
	message = request.args.get("message", None)
	button = request.args.get("b",None)
	if button == None:
		return render_template("index.html")
	else:
		return render_template("index.html", name=name)


if __name__=="__main__": 
	app.debug = True
	app.run(port=5000) 
   
