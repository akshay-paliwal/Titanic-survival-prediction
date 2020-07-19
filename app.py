# importing the necessary dependencies
from flask import Flask, render_template, request
from flask_cors import cross_origin
import pickle
import os

app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("main.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            age = float(request.form['age'])

            SibSp = float(request.form['SibSp'])
      
            Parch = float(request.form['Parch'])

            Fare = float(request.form['fare'])

            g = str(request.form['gender'])
            if g == "male":
                gender = 1.0
            elif g == "female":
                gender = 0.0
    
            c = str(request.form['Pclass'])
            if c == "First":
                Pclass = 1.0
            elif c == "Second":
                Pclass = 2.0
            elif c == "Third":
                Pclass = 3.0   


            modelname = 'modelForPrediction.sav' 
            loaded_model = pickle.load(open(modelname, 'rb')) 
            prediction = loaded_model.predict([[Pclass, gender, age, SibSp, Parch, Fare]])
            if prediction[0] == 1.0:
                val1 = "😀️ The"
                val2 = "did"
            else:
                val1 = "😢️ Sorry, The"
                val2 = "din't"

            return render_template('prediction.html', value1 = val1, value2 = val2)
        except:
            return("Something Went Wrong")
    else:
        render_template("main.html")
            
#port = int(os.getenv("PORT"))
if __name__ == "__main__":
    app.run(debug=True)
