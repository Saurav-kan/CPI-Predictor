import json
import requests
import pandas as pd
from pandas.tseries.offsets import DateOffset
from sklearn.linear_model import LinearRegression
from .models import CPIForecast

def run_cpi_forecast(start_year:int, end_year:int, horizon_months:int=1):
    # 1) Fetch CPI data from BLS API
    url     = "https://api.bls.gov/publicAPI/v2/timeseries/data/"
    headers = {'Content-Type': 'application/json'}
    payload = {
        "seriesid": ["CUUR0000SA0"],
        "startyear": str(start_year),
        "endyear":   str(end_year),
        "registrationKey": "04d45abe7d904e35bc26ff9b25c43463"
    }
    resp = requests.post(url, headers=headers, data=json.dumps(payload))
    resp.raise_for_status()
    raw_data = resp.json()["Results"]["series"][0]["data"]

    # DataFrame
    df = pd.DataFrame(raw_data)[["year","period","value"]]
    df["value"] = df["value"].astype(float)
    df["month"] = df["period"].str.extract(r"M(\d+)").astype(int)
    df["date"]  = pd.to_datetime(df.year.astype(int).map(str)
                     + "-" + df.month.map(lambda m: f"{m:02d}") + "-01")
    df = df.sort_values("date").reset_index(drop=True)
    df["lag1"] = df["value"].shift(1)
    df = df.dropna()

    
    X = df[["lag1"]]
    y = df["value"]
    model = LinearRegression().fit(X, y)

    #Predict
    last_val = df.iloc[-1]["value"]
    last_date = df.iloc[-1]["date"]
    results = []
    for i in range(1, horizon_months+1):
        pred = float(model.predict([[last_val]]))
        f_date = last_date + DateOffset(months=i)
        results.append((f_date.date(), pred))
        last_val = pred

    return results
