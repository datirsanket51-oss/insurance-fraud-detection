from flask import Flask, render_template, request, redirect, url_for
import pickle

app = Flask(__name__)

model = pickle.load(open("random_forest_model.pkl", "rb"))

# Default page → Login
@app.route('/')
def home():
    return render_template("login.html")

# Login verification
@app.route('/login', methods=['POST'])
def login():

    username = request.form['username']
    password = request.form['password']

    if username == "admin" and password == "1234":
        return render_template("index.html")
    else:
        return "Invalid Login"

@app.route('/predict', methods=['POST'])
def predict():

    # Get all form values
    features = []

    features.append(float(request.form['months_as_customer']))
    features.append(int(request.form['age']))
    features.append(int(request.form['policy_number']))
    features.append(int(request.form['policy_bind_date']))
    features.append(int(request.form['policy_state']))
    features.append(int(request.form['policy_csl']))
    features.append(int(request.form['policy_deductable']))
    features.append(int(request.form['policy_annual_premium']))
    features.append(int(request.form['umbrella_limit']))
    features.append(int(request.form['insured_zip']))
    features.append(int(request.form['insured_sex']))
    features.append(int(request.form['insured_education_level']))
    features.append(int(request.form['insured_occupation']))
    features.append(int(request.form['insured_hobbies']))
    features.append(int(request.form['insured_relationship']))
    features.append(int(request.form['capital_gains']))
    features.append(int(request.form['capital_loss']))
    features.append(int(request.form['incident_date']))
    features.append(int(request.form['incident_type']))
    features.append(int(request.form['collision_type']))
    features.append(int(request.form['incident_severity']))
    features.append(int(request.form['authorities_contacted']))
    features.append(int(request.form['incident_state']))
    features.append(int(request.form['incident_city']))
    features.append(int(request.form['incident_location']))
    features.append(int(request.form['incident_hour_of_the_day']))
    features.append(int(request.form['number_of_vehicles_involved']))
    features.append(int(request.form['property_damage']))
    features.append(int(request.form['bodily_injuries']))
    features.append(int(request.form['witnesses']))
    features.append(int(request.form['police_report_available']))
    features.append(int(request.form['total_claim_amount']))
    features.append(int(request.form['injury_claim']))
    features.append(int(request.form['property_claim']))
    features.append(int(request.form['vehicle_claim']))
    features.append(int(request.form['auto_make']))
    features.append(int(request.form['auto_model']))
    features.append(int(request.form['auto_year']))

    final_features = np.array(features).reshape(1, -1)

    prediction = model.predict(final_features)

    if prediction[0] == 1:
        result = "Fraud Claim Detected"
    else:
        result = "Legitimate Claim"

    return render_template('index.html', prediction_text=result)


if __name__ == "__main__":
    app.run(debug=True)