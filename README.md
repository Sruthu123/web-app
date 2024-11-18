**Overview**

This is a simple "To-Do List" web application built using Flask (Python). It is designed to be easy to deploy on cloud platforms like Google Cloud Platform (GCP). In this guide, we will focus on deploying the app to App Engine.

**Prerequisites**

To run this project locally or deploy it to Google Cloud, you will need the following:
•	Python 3.9
•	pip 
•	Google Cloud SDK 
•	Google Cloud account 

**Running Locally**

1.	Create project folder:
   
        commands to create:

	mkdir web-app

	cd web-app

3.	Create and activate a virtual environment
   
	commands to create:

	python -m venv venv

	venv\Scripts\activate

5.	Install Flask

    	command to create: pip install flask
  	
7.	Install the dependencies:
   
    	command to create: pip install -r requirements.txt
  	
9.	Create a file named app.yaml
   
10.	Create required files index and main
    
12.	Run the Flask app:
    
    	command to run: python app.py

The app will be accessible at http://localhost:5000/ 

**Setting up Google Cloud SDK:**

1.	Install the Google Cloud SDK.
   
2.	Authenticate with Google Cloud:
   
    	command to login: gcloud auth login
  	
3.	Set the Google Cloud project:
   
    	command to setup: gcloud config set project flask-web-app-442014
  	
**Deployment to Google Cloud**

Step 1: Set Up Google Cloud Project
1.	Go to Google Cloud Console.
2.	Create a new project.
3.	Enable Google App Engine and cloud build API in your project.
   
Step 2: Deploy the App
1.	Prepare your environment:
   
        commands Login and set
  	
        gcloud auth login
  	
        gcloud config set project YOUR_PROJECT_ID
  	
2.	Deploy the web-app:
   	 1. Make sure your project folder contains the following files:

    	• main.py
  	
    	• requirements.txt
  	
    	• app.yaml

    	command to deploy your app: gcloud app deploy

The app will be globally accessible at

https://flask-web-app-442014.el.r.appspot.com


