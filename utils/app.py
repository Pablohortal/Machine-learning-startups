# flask
from flask import Flask, request, jsonify, render_template
import numpy as np
#import pickle
import joblib

app = Flask(__name__) # create an instance of the Flask class

#load model
model = joblib.load('pablo.joblib')
scaler = joblib.load('scaler.joblib')
label_encoder = joblib.load('label_encoder.joblib')
label_encoder_2 = joblib.load('prueba_33.joblib')
# star flask
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    features = [x for x in request.form.values()]
    print(features)
    country = label_encoder.transform([features[0]])[0]
    Industry = label_encoder_2.transform([features[1]])[0]
    features[0] = country
    features[1] = Industry
    #colums = ['year', 'num_investors', 'industry', 'country']
    final_features = [np.array([int(x) for x in features])] #crear data frame con colummnas y entradas en orden   

    
    prediction = model.predict(final_features)


    return render_template('index.html', prediction_text='Tu empresa tiene un valor de {}'.format(round(prediction[0],3)))

if __name__ == "__main__":
    app.run(port=80)