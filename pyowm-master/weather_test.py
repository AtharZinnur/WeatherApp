from pyowm.owm import OWM
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")

print("Loaded API key:", api_key)  # To confirm it loads
print(f">{api_key}<")
owm = OWM(api_key)  # <--- use variable here
mgr = owm.weather_manager()

observation = mgr.weather_at_place('London,GB')
w = observation.weather

print("Weather status:", w.detailed_status)
print("Temperature (°C):", w.temperature('celsius')["temp"])
print("Humidity (%):", w.humidity)
print("Wind speed (m/s):", w.wind()['speed'])