from flask import Flask, render_template, request,url_for
import jsonify
import requests
import pickle
app = Flask(__name__)  
model = pickle.load(open('model1.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")
    
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
#1
        Year = int(request.form['Year'])                
#2
        Volume=float(request.form['Volume'])
    #3
        Mileage=float(request.form['Mileage'])
#4
        Fuel=request.form['Fuel']
        if(Fuel=='Petrol'):
                Fuel=0
        else:
            Fuel=1
    #5
        Transmission=request.form['Transmission']
        if(Transmission=='Mechanic'):
            Transmission=0
        else:
            Transmission=1

        prediction=model.predict([[Year,Mileage,Fuel,Volume,Transmission]])
        output=round(prediction[0])
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('result.html',result="Your car price in USD {}".format(output))
            
    else:
        return render_template('index.html')
if __name__=="__main__":
    app.run(debug=True)

