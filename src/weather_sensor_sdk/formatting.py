from .calculation import celsius_to_fahrenheit
from .models import SensorData
from .wind_classification import classify_wind_speed


def format_weather(normalized_data: SensorData, feels_like: float) -> str:
    temperature_celsius = normalized_data["temperature_celsius"]
    temperature_fahrenheit = celsius_to_fahrenheit(temperature_celsius)
    wind_classification = classify_wind_speed(normalized_data["wind_speed_mps"])

    return f"Weather in {normalized_data['location']}: {temperature_celsius:.1f}°C ({temperature_fahrenheit:.1f}°F), humidity: {normalized_data['humidity_percent']:.1f}%. Feels like: {feels_like:.1f}°C. Wind: {wind_classification}."
