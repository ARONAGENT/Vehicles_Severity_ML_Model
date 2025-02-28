# Vehicle Severity Prediction - Django & Machine Learning

## Overview
This is a Django-based Machine Learning project that predicts the severity of a vehicle accident based on various input factors such as speed, weather conditions, road type, and more. The model categorizes severity into **Minor, Major, or Fatal**.

## Features
- **User Input**: Takes accident-related inputs from users.
- **Prediction Model**: Uses a trained ML model to predict accident severity.
- **Django Integration**: The ML model is deployed within a Django web application.
- **REST API Support**: Allows API calls for predictions.

## Dataset & Inputs
The ML model is trained on accident data and considers the following factors:

1. **Speed** (in km/hr)
2. **Weather Condition**
   - 1 = Clear
   - 2 = Rainy
   - 3 = Fog
3. **Road Type**
   - 1 = Highway
   - 2 = City Road
   - 3 = Rural Road
4. **Time of Day**
   - 1 = Morning
   - 2 = Afternoon
   - 3 = Night
5. **Vehicle Type**
   - 1 = Car
   - 2 = Motorcycle
   - 3 = Truck
6. **Traffic Density**
   - 1 = Low
   - 2 = Medium
   - 3 = High

## Prediction Categories
- **Minor**: Low severity accidents
- **Major**: Moderate severity accidents
- **Fatal**: High severity accidents
  <br><br>
**Execution Video ->**

  

https://github.com/user-attachments/assets/562f8948-b59c-4ee5-b53b-35ea41ab97f1


  
## Installation Guide
Follow these steps to set up and run the project locally:

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/vehicle-severity-ml.git
cd vehicle-severity-ml
```

### Step 2: Create a Virtual Environment
```bash
virtualenv mlproject
mlproject\Scripts\
use activate to activate the virtual environment
```

### Step 3: Install Dependencies
```bash
pip install django
pip install joblib
pip install sckit-learn
```

### Step 4: Create a Django Project
```bash
django-admin startproject vehicleSeverity
cd vehicleServerty 
```

### Step 6: Run the Django Server
```bash
python manage.py runserver
```

### Step 7: Access the Application
Open your browser and visit:  
**http://127.0.0.1:8000/**

## API Endpoints
The application provides REST API endpoints:

### 1. Predict Severity
**Endpoint:** `/predict/`  
**Method:** `POST`  
**Request Body (JSON):**
```json
{
  "speed": 80,
  "weather": 2,
  "road_type": 1,
  "time_of_day": 3,
  "vehicle_type": 1,
  "traffic_density": 3
}
```
**Response:**
```json
{
  "severity": "Major"
}
```

## Conclusion
This project successfully integrates a Machine Learning model with Django to predict vehicle accident severity. It allows users to input accident conditions and receive a severity prediction instantly.

## Clone the Repo & Done ✅
```bash
git clone https://github.com/ARONAGENT/vehicle-severity-ml.git
```

🚀 **Happy Coding!**

