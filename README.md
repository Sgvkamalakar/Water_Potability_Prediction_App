## Water Potability Prediction App using Gradio

The main objective of this project is to provide a simple and easy-to-use web application that can predict the potability of water by analyzing the given parameters. The web application is built using Gradio, a Python library that helps to quickly create customizable UI components for machine learning models. The application allows the user to input the various water parameters and get an immediate prediction of the water potability.

This repository contains the code for both the machine learning model and the Gradio web application. 

The dataset used for building the model is available in the repository as a CSV file. The dataset contains a total of 3276 observations of water quality parameters and the target variable 'Potability'. The data is preprocessed, cleaned, and transformed before being used to train the machine learning model.

Overall, this project is an excellent demonstration of how machine learning and web development can be combined to create a useful application for predicting water potability. The code and documentation in this repository can be used as a starting point for similar projects in the future.

This documentation note is intended to provide a step-by-step guide for using the application, as well as an overview of the model and its implementation.

#### System Requirements:
* Python 3.7 or higher
* Required Python Libraries: pandas, numpy, sklearn, gradio

#### Getting Started:
* Clone the GitHub repository
* Install the required libraries using pip or conda
* Run the Gradio app using the command 'py predict.py'
* Access the app using a web browser and the provided URL

#### Using the App:
Once the app is launched in the web browser, input the various water parameters in the provided fields.
Click on the "Submit" button to get the water potability prediction.
The prediction will be displayed in the "Result" field.

#### Understanding the Model:
The model is built using Python and Scikit-learn libraries. It uses a Random Forest Classifier algorithm to predict the potability of water based on the given parameters. The dataset used for building the model is available in the repository as a CSV file. The data is preprocessed, cleaned, and transformed before being used to train the machine learning model.

#### Conclusion:
The Water Potability Prediction App using Gradio is an excellent example of how machine learning and web development can be combined to create a useful application. This documentation note provides a step-by-step guide for using the application and an overview of the model and its implementation. The code and documentation in this repository can be used as a starting point for similar projects in the future.
