from flask import Flask, render_template

app = Flask(__name__)
import joblib as joblib

features = [4, 2.5, 3000, 15, 17903.0, 1]
beds = features[0]
baths = features[1]
Sqft = features[2]
Age = features[3]
Lotsize = features[4]
Garage = features[5]

@app.route('/')
def index():

    return render_template('index.html', Beds=beds, Baths=baths, Sqft=Sqft,
                           Age=Age, Lotsize=Lotsize, Garage=Garage)

@app.route('/linear_regression')
def linear_regression():
    model = joblib.load('./notebooks/regr.pkl')
    # Make prediction - features = ['BEDS', 'BATHS', 'SQFT', 'AGE', 'LOTSIZE', 'GARAGE']
    prediction = model.predict([[4, 2.5, 3000, 15, 17903.0, 1]])[0][0].round(1)
    prediction = str(prediction)
    return render_template('index.html', price=prediction, Beds=beds, Baths=baths, Sqft=Sqft,
                           Age=Age, Lotsize=Lotsize, Garage=Garage)

@app.route('/train_test_split')
def train_test_split():
    model = joblib.load('./notebooks/train_test_split.pkl')
    # Make prediction - features = ['BEDS', 'BATHS', 'SQFT', 'AGE', 'LOTSIZE', 'GARAGE']
    prediction = model.predict([[4, 2.5, 3000, 15, 17903.0, 1]])[0][0].round(1)
    prediction = str(prediction)
    return render_template('index.html', price=prediction, Beds=beds, Baths=baths, Sqft=Sqft,
                           Age=Age, Lotsize=Lotsize, Garage=Garage)

@app.route('/decision_tree')
def decision_tree():
    model = joblib.load('./notebooks/decision_tree.pkl')
    # Make prediction - features = ['BEDS', 'BATHS', 'SQFT', 'AGE', 'LOTSIZE', 'GARAGE']
    prediction = model.predict([[4, 2.5, 3000, 15, 17903.0, 1]])[0].round(1)
    prediction = str(prediction)
    return render_template('index.html', price=prediction, Beds=beds, Baths=baths, Sqft=Sqft,
                           Age=Age, Lotsize=Lotsize, Garage=Garage)

@app.route('/random_forest')
def random_forest():
    model = joblib.load('./notebooks/random_forest.pkl')
    # Make prediction - features = ['BEDS', 'BATHS', 'SQFT', 'AGE', 'LOTSIZE', 'GARAGE']
    prediction = model.predict([[4, 2.5, 3000, 15, 17903.0, 1]])[0].round(1)
    prediction = str(prediction)
    return render_template('index.html', price=prediction, Beds=beds, Baths=baths, Sqft=Sqft,
                           Age=Age, Lotsize=Lotsize, Garage=Garage)