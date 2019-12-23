from flask import Flask,render_template,request,session,redirect,url_for

app=Flask(__name__)

app.secret_key="secret"

@app.route("/",methods=["GET","POST"])

def index():
	try:
		balance=session["balance"]
		cnt=session["cnt"]
	except KeyError:
		balance=session["balance"]=8000
		cnt=session["cnt"]=0

	if request.method=="GET":
		return render_template("index.html",balance=balance,cnt=cnt)

	if request.method=="POST":
		if session["cnt"]==5:
			return render_template("index.html",balance=balance,cnt=cnt,msg="Transaction limit exceeded")

		if(request.form["action"]=="deposit" and session["cnt"]!=5):
			balance+=int(request.form["amount"])
			session["balance"]=balance
			cnt+=1
			session["cnt"]=cnt
			return render_template("index.html",msg="Deposited",balance=balance,cnt=cnt)

		if(request.form["action"]=="withdraw" and int(request.form["amount"])<=session["balance"] and session["cnt"]!=5):
			balance-=int(request.form["amount"])
			session["balance"]=balance
			cnt+=1
			session["cnt"]=cnt
			return render_template("index.html",msg="Withdrawn",balance=balance,cnt=cnt)

		else:
			return render_template("index.html",msg="Insufficient funds",balance=balance,cnt=cnt)



if __name__=="__main__":
	app.run(debug=True)








