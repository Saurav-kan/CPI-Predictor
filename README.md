# CPI Predictor

A lightweight Django app that fetches U.S. CPI data, trains a simple lag-1 linear model, and lets you predict future CPI
Allows you to range of years to train the model over allowing testing of previous years based on information before that selected year

---

Featutures: 

- Pulls monthly CPI-U series from the BLS API  
- Trains a one-lag LinearRegression (scikit-learn)  
- Forecasts n-months ahead (iteratively)  
- Persists predictions in a Django model  
- REST API (DRF) at `/api/cpi/`  
- Minimal HTML dashboard with form inputs  

---

Stack and Dependencies:

- **Python** 3.8+  
- **Django** 4.x  
- **Django REST Framework**  
- **pandas** (⎯data wrangling)  
- **scikit-learn** (⎯LinearRegression)  
- **requests** (⎯BLS API calls)  

---

To use: 
1. Clone Repository
2. Dowload Dependencies from requirements.txt
3. Run
  '''bash
python manage.py runserver from terminal

