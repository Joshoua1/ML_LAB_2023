# Diabetes Prediction Web Application

This is a web application built using Flask that predicts the likelihood of diabetes based on user input. The application utilizes a Decision Tree Classifier trained on a diabetes dataset to provide predictions.

## Features

- User-friendly interface for inputting health data.
- Real-time predictions based on user inputs.
- Dynamic and visually appealing design using Bootstrap.
- Color-coded output to indicate prediction results (positive or negative).
- Basic input validation to ensure realistic data entry.

## Technologies Used

- **Python**: Programming language for backend development.
- **Flask**: Web framework for building the web application.
- **scikit-learn**: Library for machine learning to train the Decision Tree model.
- **Pandas**: Data manipulation library used to handle the dataset.
- **Bootstrap**: CSS framework for responsive design.
- **HTML/CSS/JavaScript**: Frontend technologies for building the user interface.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- pip (Python package installer)

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Joshoua1/ML_LAB_2023.git
   cd Decision Tree
   ```
   
2. **Install required packages**:

    You can create a virtual environment (recommended) and install the necessary packages:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install Flask pandas scikit-learn
    ```

3. **Download the dataset**:

    Ensure you have the diabetes_dataset.csv file in your project directory. This file is required to train the model.

4. **Train and save the model**:

    Run the following script to train your model and save it as diabetes_model.pkl:
    ```bash
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.tree import DecisionTreeClassifier
    import pickle

    # Load the dataset
    df = pd.read_csv("diabetes_dataset.csv")

    # Prepare data
    X = df.drop("Outcome", axis=1)
    y = df["Outcome"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    clf = DecisionTreeClassifier(random_state=42)
    clf.fit(X_train, y_train)

    # Save the model using pickle
    with open('diabetes_model.pkl', 'wb') as model_file:
        pickle.dump(clf, model_file)
    ```
    
## Running the Application

1. Start the Flask application:

    ```bash
    python app.py
    ```

2. Open your web browser and navigate to http://127.0.0.1:5000/ to access the diabetes prediction application.

## Usage

1. Fill in the required fields in the form with your health data.
2. Click on the "Predict" button to receive a prediction regarding your likelihood of having diabetes.
3. The result will be displayed below the form with color-coded feedback.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments


### Instructions for Use

1. Replace `https://github.com/Joshoua1/ML_LAB_2023.git` an duse the Decision Tree folder.
2. If you have a license file, make sure to include it in your project directory and reference it in this README.
3. Adjust any sections as necessary based on your specific implementation details or additional features you may have added.

This README provides a comprehensive overview of your project, making it easier for others (or yourself in the future) to understand how to set up and use your diabetes prediction web application!

![image](https://github.com/user-attachments/assets/5435b306-a536-40bf-9e97-9435d53d264e)

