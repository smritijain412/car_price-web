from flask import Flask, render_template, request
import jsonify
import requests
import pickle
app = Flask(__name__)  
model = pickle.load(open('models.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':

        Year = int(request.form['Year'])
        Volume=float(request.form['Volume'])
        Fuel_Type=request.form['Fuel_Type']
        if(Fuel_Type=='Petrol'):
                Fuel_Type=0
        else:
            Fuel_Type=1
        condition=request.form['condition']
        if(condition=='with mileage'):
            condition=1
        else:
            condition=0
        Transmission_Mannual=request.form['Transmission_Mannual']
        if(Transmission_Mannual=='Mechanic'):
            Transmission_Mannual=0
        else:
            Transmission_Mannual=1
        prediction=model.predict([[Year,Volume,Fuel_Type,condition,Transmission_Mannual]])
        output=round(prediction[0])
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('result.html',result="Your car price in USD {}".format(output))
            
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

