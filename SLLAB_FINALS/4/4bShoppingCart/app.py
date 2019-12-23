from flask import Flask,request,render_template,url_for,redirect,session
app=Flask(__name__)

app.secret_key="hello"

@app.route("/",methods=["GET","POST"])

def index():
	if request.method=="GET":
		return render_template("index.html")

	if request.method=="POST":
		for item in ["EGGS","MILK","BREAD"]:
			if item not in session:
				session[item]=int(request.form[item])
			else:
				session[item]+=int(request.form[item])
		return redirect(url_for('cart'))

@app.route("/cart",methods=["GET","POST"])

def cart():
	cart=[]
	for item in ["EGGS","MILK","BREAD"]:
		cart.append({"name":item,"qty":session[item]})

	return render_template("cart.html",cart=cart)

if __name__=="__main__":
	app.run(debug=True)





