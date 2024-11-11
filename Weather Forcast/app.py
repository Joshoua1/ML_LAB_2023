from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# Load data and train the model
data = pd.read_csv("weather_forecast_data.csv")
label_encoder = LabelEncoder()
data['Rain'] = label_encoder.fit_transform(data['Rain'])

X = data.drop('Rain', axis=1)  
y = data['Rain']

rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X, y)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.get_json()  # Get JSON data from request
    
    # Accessing values from the JSON data
    temperature = float(input_data['temperature'])
    humidity = float(input_data['humidity'])
    wind_speed = float(input_data['wind_speed'])
    cloud_cover = float(input_data['cloud_cover'])
    pressure = float(input_data['pressure'])

    input_features = [[temperature, humidity, wind_speed, cloud_cover, pressure]]
    
    prediction = rf_model.predict(input_features)
    
    result = "Rain" if prediction[0] == 1 else "No Rain"
    
    return jsonify(prediction=result)

if __name__ == '__main__':
    app.run(debug=True)