from flask import Flask,render_template,redirect,url_for,request,session
import re
import time

app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def register():
    if request.method== "GET":
        return render_template("index.html")
    
    if request.method== "POST":

        patternusn="^[1][A-Z][A-Z][0-9][0-9][A-Z][A-Z][0-9][0-9][0-9]$"
        if not re.match(patternusn,request.form["usn"]):
            msg="Invalid USN"
            return render_template("index.html",msg=msg)
        
        try:
            time.strptime(request.form["dob"],"%d/%m/%Y")
        except ValueError:
            msg="Date Format Invalid"
            return render_template("index.html",msg=msg)
        
        sum=int(request.form["m1"])+int(request.form["m2"])+int(request.form["m3"])
        avg=int(sum/3)
        msg="Registered"
        return render_template('result.html',msg=msg,usn=request.form["usn"],avg=avg)

if __name__=='__main__':
    app.run(debug=True)


