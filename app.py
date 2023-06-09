from flask import Flask,render_template,request
import pickle

app=Flask(__name__)

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/pred",methods=["POST"])
def pred():
	msg=""
	age=int(request.form["age"])
	sex=int(request.form["sex"])
	cp=int(request.form["cp"])
	thalachh=int(request.form["thalachh"])
	thall=int(request.form["thall"])
	with open("heart.model","rb") as f:
		model=pickle.load(f)
	d=[[age,sex,cp,thalachh,thall]]
	res=model.predict(d)[0]
	if res==0:	msg="Heart disease NOT detected"
	elif res==1:	msg="Heart disease detected!!"
	return render_template("home.html",msg=msg)

if __name__=="__main__":
	app.run(debug=True,use_reloader=True)
