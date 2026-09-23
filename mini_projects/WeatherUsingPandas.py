import requests
import pandas as pd

latitude = 13.0827
longitude = 80.2707

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": latitude,
    "longitude": longitude,
    "daily": "temperature_2m_max,temperature_2m_min",
}

response = requests.get(url, params=params, timeout=10)

print("Status:", response.status_code)

response.raise_for_status()

data = response.json()

daily_data = data["daily"]

df = pd.DataFrame({
    "date": daily_data["time"],
    "max_temp": daily_data["temperature_2m_max"],
    "min_temp": daily_data["temperature_2m_min"],
})

df["date"] = pd.to_datetime(df["date"])

print(df)