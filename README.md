# Vehicle Severity Prediction - Django & Machine Learning

[![Django](https://img.shields.io/badge/Django-5.x-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.x-orange.svg)](https://scikit-learn.org/)
[![Machine Learning](https://img.shields.io/badge/ML-Prediction%20Model-red.svg)](https://en.wikipedia.org/wiki/Machine_learning)
[![Joblib](https://img.shields.io/badge/Joblib-Model%20Serialization-yellow.svg)](https://joblib.readthedocs.io/)
[![REST API](https://img.shields.io/badge/REST-API-purple.svg)](https://restfulapi.net/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.x-blueviolet.svg)](https://getbootstrap.com/)

## 📋 Project Overview

This Django-based Machine Learning application predicts vehicle accident severity using a trained classification model. The system analyzes various accident-related factors such as speed, weather conditions, road type, and traffic density to categorize accidents into **Minor**, **Major**, or **Fatal** severity levels. The ML model is seamlessly integrated into a Django web application with both web interface and REST API support.

## 🚗 Demo Video

https://github.com/user-attachments/assets/562f8948-b59c-4ee5-b53b-35ea41ab97f1

*Complete demonstration of vehicle accident severity prediction system!*

## ✨ Key Features

### Core Functionality
- 🎯 **Accident Severity Prediction** - ML-powered classification system
- 📊 **Multi-Factor Analysis** - Considers 6 key accident parameters
- 🌐 **Web Interface** - User-friendly form for input data
- 🔗 **REST API** - JSON-based prediction endpoints
- 📱 **Responsive Design** - Mobile-friendly interface
- ⚡ **Real-Time Predictions** - Instant severity assessment

### Machine Learning Features
- **Classification Model** - Trained on historical accident data
- **Feature Engineering** - Optimized input parameter encoding
- **Model Serialization** - Joblib-based model persistence
- **Prediction Categories** - Three-tier severity classification
- **Input Validation** - Robust data preprocessing

## 🛠️ Technology Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| **Django** | 5.x | Web Framework |
| **Python** | 3.x | Backend Language |
| **Scikit-Learn** | 1.x | Machine Learning Library |
| **Joblib** | Latest | Model Serialization |
| **NumPy** | Latest | Numerical Computing |
| **Pandas** | Latest | Data Processing |
| **Bootstrap** | 5.x | UI Framework |
| **HTML/CSS/JS** | Latest | Frontend Technologies |

## 🧠 Machine Learning Model

### Input Parameters

The prediction model analyzes the following accident factors:

#### 1. **Speed** (Continuous Variable)
- **Type**: Integer (km/hr)
- **Range**: 0-200 km/hr
- **Impact**: Higher speeds typically increase severity

#### 2. **Weather Condition** (Categorical)
| Code | Condition | Description |
|------|-----------|-------------|
| 1 | Clear | Optimal visibility and road conditions |
| 2 | Rainy | Reduced visibility and slippery roads |
| 3 | Fog | Severely limited visibility |

#### 3. **Road Type** (Categorical)
| Code | Type | Characteristics |
|------|------|----------------|
| 1 | Highway | High-speed, controlled access roads |
| 2 | City Road | Urban streets with traffic signals |
| 3 | Rural Road | Less maintained, narrow roads |

#### 4. **Time of Day** (Categorical)
| Code | Period | Risk Factors |
|------|--------|--------------|
| 1 | Morning | Rush hour traffic, commuter patterns |
| 2 | Afternoon | Peak traffic, good visibility |
| 3 | Night | Reduced visibility, fatigue factors |

#### 5. **Vehicle Type** (Categorical)
| Code | Type | Vulnerability Level |
|------|------|-------------------|
| 1 | Car | Moderate protection |
| 2 | Motorcycle | High vulnerability |
| 3 | Truck | Heavy vehicle impact |

#### 6. **Traffic Density** (Categorical)
| Code | Density | Impact on Accidents |
|------|---------|-------------------|
| 1 | Low | Higher speeds, fewer obstacles |
| 2 | Medium | Moderate congestion |
| 3 | High | Stop-and-go traffic, multi-vehicle risks |

### Prediction Categories

The model classifies accidents into three severity levels:

| Severity | Description | Characteristics |
|----------|-------------|-----------------|
| **Minor** | Low-impact accidents | Property damage, minor injuries |
| **Major** | Moderate-impact accidents | Significant injuries, hospitalization |
| **Fatal** | High-impact accidents | Life-threatening or fatal outcomes |

### Model Architecture

```python
# Example model pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# Model pipeline
model_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        random_state=42
    ))
])
```

## 🚀 Installation & Setup

### Prerequisites

Ensure you have the following installed:
- **Python 3.8+**
- **pip** (Python package manager)
- **Git**
- **Virtual Environment** (recommended)

### Step-by-Step Installation

#### 1. **Clone the Repository**
```bash
git clone https://github.com/ARONAGENT/vehicle-severity-ml.git
cd vehicle-severity-ml
```

#### 2. **Create Virtual Environment**
```bash
# Create virtual environment
python -m venv mlproject

# Activate virtual environment
# Windows:
mlproject\Scripts\activate

# macOS/Linux:
source mlproject/bin/activate
```

#### 3. **Install Dependencies**
```bash
# Core dependencies
pip install django
pip install scikit-learn
pip install joblib
pip install numpy
pip install pandas

# Additional packages
pip install matplotlib  # For data visualization
pip install seaborn     # For advanced plotting
pip install requests    # For API testing
```

#### 4. **Create Django Project Structure**
```bash
# Create Django project
django-admin startproject vehicleSeverity
cd vehicleSeverity

# Create Django app
python manage.py startapp ml_predictor
```

#### 5. **Configure Django Settings**

Update `settings.py`:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ml_predictor',  # Add your ML app
]

# Static files configuration
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

# Media files for model storage
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"
```

#### 6. **Run Database Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

#### 7. **Start Development Server**
```bash
python manage.py runserver
```

#### 8. **Access the Application**
Visit `http://127.0.0.1:8000/` to use the prediction interface.

## 📁 Project Structure

```
vehicle-severity-ml/
├── vehicleSeverity/
│   ├── vehicleSeverity/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   ├── ml_predictor/
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── forms.py
│   │   └── ml_utils.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── prediction_form.html
│   │   ├── prediction_result.html
│   │   └── api_docs.html
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── js/
│   │   │   └── prediction.js
│   │   └── images/
│   ├── models/
│   │   ├── severity_model.pkl
│   │   └── scaler.pkl
│   ├── data/
│   │   ├── training_data.csv
│   │   └── model_metrics.json
│   └── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 🔗 API Documentation

### REST API Endpoints

#### 1. **Predict Accident Severity**
```http
POST /api/predict/
Content-Type: application/json
```

**Request Body:**
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
    "severity": "Major",
    "confidence": 0.85,
    "factors": {
        "speed": "High risk factor",
        "weather": "Moderate risk",
        "night_time": "Increased risk"
    },
    "recommendation": "Exercise extreme caution"
}
```

#### 2. **Get Model Information**
```http
GET /api/model-info/
```

**Response:**
```json
{
    "model_type": "Random Forest Classifier",
    "accuracy": 0.89,
    "features": [
        "speed", "weather", "road_type", 
        "time_of_day", "vehicle_type", "traffic_density"
    ],
    "categories": ["Minor", "Major", "Fatal"],
    "last_trained": "2024-01-15"
}
```

#### 3. **Batch Predictions**
```http
POST /api/predict-batch/
Content-Type: application/json
```

**Request Body:**
```json
{
    "predictions": [
        {
            "speed": 60,
            "weather": 1,
            "road_type": 2,
            "time_of_day": 1,
            "vehicle_type": 1,
            "traffic_density": 2
        },
        {
            "speed": 120,
            "weather": 3,
            "road_type": 1,
            "time_of_day": 3,
            "vehicle_type": 2,
            "traffic_density": 1
        }
    ]
}
```


## 📊 Model Performance

### Metrics
- **Accuracy**: 89.2%
- **Precision**: 87.5% (weighted average)
- **Recall**: 89.2% (weighted average)
- **F1-Score**: 88.3% (weighted average)

### Feature Importance
| Feature | Importance | Impact |
|---------|------------|--------|
| Speed | 35.2% | Primary risk factor |
| Vehicle Type | 18.7% | Vulnerability level |
| Weather | 16.3% | Visibility/road conditions |
| Traffic Density | 12.8% | Collision probability |
| Road Type | 10.5% | Infrastructure safety |
| Time of Day | 6.5% | Visibility/alertness |

## 📈 Future Enhancements

### Planned Features
- **Real-time Data Integration** - Traffic and weather APIs
- **Geographic Factors** - Location-based risk assessment
- **Historical Analysis** - Trend analysis and reporting
- **Mobile App** - Native iOS/Android applications
- **Advanced Models** - Deep learning implementations

### Model Improvements
- **Ensemble Methods** - Combining multiple algorithms
- **Feature Engineering** - Additional risk factors
- **Real-time Learning** - Continuous model updates
- **Explainable AI** - Model interpretability features

### Contribution Areas
- **Model Optimization** - Improve prediction accuracy
- **Feature Engineering** - Add new input parameters
- **UI/UX Enhancement** - Better user interface
- **API Expansion** - Additional endpoints
- **Documentation** - Code and usage documentation
  
## 👥 Authors & Contributors

- **[ARONAGENT](https://github.com/ARONAGENT)** - Project Creator & Maintainer

## 🙏 Acknowledgments

- **Scikit-Learn Team** - For the excellent ML library
- **Django Community** - For the robust web framework
- **Traffic Safety Organizations** - For research and data insights
- **Open Source Community** - For continuous support and inspiration

## 📞 Support & Contact

### Getting Help
- 📖 **Documentation**: Check this README first
- 🐛 **Bug Reports**: [Create an Issue](https://github.com/ARONAGENT/vehicle-severity-ml/issues)
- 💡 **Feature Requests**: [Suggest Features](https://github.com/ARONAGENT/vehicle-severity-ml/issues)
- 💬 **Questions**: [Start a Discussion](https://github.com/ARONAGENT/vehicle-severity-ml/discussions)

### Connect with the Developer
- **GitHub**: [@ARONAGENT](https://github.com/ARONAGENT)
- **LinkedIn**: [Connect for professional inquiries](https://www.linkedin.com/in/aronagent/)

## 🎯 Learning Outcomes

This project demonstrates:
- **Machine Learning Integration** with web frameworks
- **Classification Model** development and deployment
- **REST API** design and implementation
- **Real-world Problem Solving** with ML
- **Full-stack Development** with Django
- **Model Deployment** and production considerations

---

⭐ **If you find this project helpful, please give it a star!** ⭐

*Built with ❤️ using Django, Scikit-Learn, and modern ML practices*
