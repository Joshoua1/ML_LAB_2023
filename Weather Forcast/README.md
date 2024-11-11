# Weather Forecast Prediction Application

This is a simple web application that predicts whether it will rain based on user-provided weather parameters such as temperature, humidity, wind speed, cloud cover, and pressure. The application uses a Random Forest Classifier model trained on historical weather data.

## Features

- User-friendly interface for inputting weather parameters.
- Predicts rain or no rain based on the input data.
- Displays the prediction result dynamically without page refresh.
- Responsive design for mobile and desktop users.

## Technologies Used

- **Python**: Backend logic using Flask framework.
- **Pandas**: Data manipulation and analysis.
- **Scikit-learn**: Machine learning model for prediction.
- **HTML/CSS**: Frontend structure and styling.
- **JavaScript**: Dynamic interaction with the backend.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- pip (Python package installer)

## Installation

1. Clone this repository to your local machine:
```bash
git clone git@github.com:Joshoua1/ML_LAB_2023.git
```
Use the Weather forcast folder

2. Navigate to the project directory:
```bash
cd weather-forecast-prediction
```

3. Install the required Python packages:
```bash
pip install Flask pandas scikit-learn seaborn matplotlib
```

4. Place your weather dataset in the project directory and name it 
    'weather_forecast_data.csv'.

# Usage

1. Run the Flask application:
```bash
python app.py
```

2. Open your web browser and go to http://127.0.0.1:5000/.

3. Enter the required weather parameters in the form and click "Predict".

4. The application will display whether it predicts "Rain" or "No Rain".
Project Structure.
```bash
text
/weather-forecast-prediction
    ├── app.py                     # Main application file
    ├── weather_forecast_data.csv  # Dataset for training the model
    ├── /static                    # Directory for static files (CSS, images)
    │   ├── styles.css             # CSS styles for the application
    └── /templates                 # Directory for HTML templates
        └── index.html             # Main HTML file for the application
```

# Contributing
Contributions are welcome! If you have suggestions or improvements, feel free to submit a pull request.
