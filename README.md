# CardioPred: Predict if you have a heart disease

Dataset link:
https://www.kaggle.com/datasets/rashikrahmanpritom/heart-attack-analysis-prediction-dataset


"CardioPred" is a heart disease prediction application, which takes as input the details like chest pain type, thalassemic or not, blood pressure etc. The prediction of the heart condition is done using AdaboostClassifier, which uses the RandomForestClassifier internally, as the base estimator. This model is 76% accurate (do refer to the .ipynb file)

## Deployment

To deploy this project run

```bash
  python app.py
```


## Tech Stack

**Client:** HTML, CSS

**Server:** Flask, PythonAnywhere

**Storage:** sqlite3




