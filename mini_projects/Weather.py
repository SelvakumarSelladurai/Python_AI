import requests
from datetime import datetime, timedelta

latitude = 13.0827
longitude = 80.2707

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

response = requests.get(url)
data = response.json()

print(data)
print(data["current"])

# {
#     'latitude': 13.110721,
#     'longitude': 80.2459, 
#     'generationtime_ms': 0.02276897430419922, 
#     'utc_offset_seconds': 0, 
#     'timezone': 'GMT', 
#     'timezone_abbreviation': 'GMT', 
#     'elevation': 12.0, 
#     'current_units': {
#         'time': 'iso8601', 
#         'interval': 'seconds', 
#         'temperature_2m': '°C'
#     }, 
#     'current': {
#         'time': '2026-09-23T15:00', 
#         'interval': 900, 
#         'temperature_2m': 28.4
#     }
# }

# {
#     'time': '2026-09-23T15:00', 
#     'interval': 900, 
#     'temperature_2m': 28.4
# }

def get_weather(latitude, longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m")
    data = response.json()
    return data['current']['temperature_2m']

# Get temperature for different cities
paris_temp = get_weather(48.85, 2.35)
london_temp = get_weather(51.50, -0.12)
tokyo_temp = get_weather(35.68, 139.69)

print(f"Paris: {paris_temp}°C")
print(f"London: {london_temp}°C")
print(f"Tokyo: {tokyo_temp}°C")


# Calculate dates
today = datetime.now()
week_ago = today - timedelta(days=7)

# Format dates for API (YYYY-MM-DD)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

# Get Paris weather for past week
url1 = f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url1)
data2 = response.json()
print(data2)
