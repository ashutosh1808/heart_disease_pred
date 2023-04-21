import pickle

with open("heart.model","rb") as f:
	model=pickle.load(f)


age=int(input("enter age: "))
sex=int(input("enter sex (0-male, 1-female): "))
cp=int(input("enter chest pain type: "))
trtbps=int(input("enter resting bloodpressure: "))
chol=int(input("enter cholesterol: "))
fbs=int(input("fasting sugar - 0=false, 1=true : "))
restecg=int(input("enter resting ecg (0=normal,1=abnormal, 2= definite left ventricles): "))
thalachh=int(input("enter max heart rate: "))
exng=int(input("exercise reduced angina (1=yes,0=no): "))
oldpeak=int(input("enter previous peak: "))
slp=int(input("enter slope of peak exercise: "))
caa=int(input("enter no of major vessels (0-3): "))
thall=int(input("enter thalassemia: "))
d=[[age,sex,cp,trtbps,chol,fbs,restecg,thalachh,exng,oldpeak,slp,caa,thall]]
print(model.predict(d))