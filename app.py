import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle

app=Flask(__name__)

model=pickle.load(open('gas.pkl','rb')) 

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    x_test=[int(x) for x in request.form.values()]
    x_test = [np.array(x_test)]
    prediction=model.predict(x_test)
    print(prediction)
    pred=prediction[[0]]
    return render_template('index.html',prediction_text='Gas Price is {} dollors'.format(pred))
if __name__=="__main__":
    app.run(debug=True)
    
    
    
