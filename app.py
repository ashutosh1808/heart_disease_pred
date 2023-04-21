from flask import Flask,render_template,request
import pickle

app=Flask(__name__)

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/pred",methods=["POST"])
def pred():
	age=int(request.form["age"])
	sex=int(request.form["sex"])
	cp=int(request.form["cp"])
	trtbps=int(request.form["trtbps"])
	chol=int(request.form["chol"])
	fbs=int(request.form["fbs"])
	restecg=int(request.form["restecg"])
	thalachh=int(request.form["thalachh"])
	exng=int(request.form["exng"])
	oldpeak=float(request.form["oldpeak"])
	slp=float(request.form["slp"])
	caa=int(request.form["caa"])
	thall=int(request.form["thall"])
	with open("heart.model","rb") as f:
		model=pickle.load(f)
	d=[[age,sex,cp,trtbps,chol,fbs,restecg,thalachh,exng,oldpeak,slp,caa,thall]]
	res=model.predict(d)
	return render_template("home.html",msg=res)

if __name__=="__main__":
	app.run(debug=True,use_reloader=True)