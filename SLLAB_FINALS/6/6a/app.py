from flask import Flask,request,session,redirect,url_for,render_template

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])

def index():
	if request.method=="GET":
		return render_template('index.html')

	if request.method=="POST":
		if(request.form["price1"].isdigit() and request.form["price2"].isdigit() and request.form["price3"].isdigit()):
			total=int(request.form["price1"])+int(request.form["price2"])+int(request.form["price3"])
			msg="Total Price:"+str(total)
			return render_template('index.html',msg=msg)

		else:
			msg="Invalid price! Please ensure you fill all fields correctly"
			return render_template('index.html',msg=msg)


if __name__=='__main__':
	app.run(debug=True)


