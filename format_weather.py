from sensor_types import SensorData
from temperature_utils import celsius_to_fahrenheit


def format_weather(normalized_data: SensorData, feels_like: float) -> str:
    temperature_celsius = normalized_data["temperature_celsius"]
    temperature_fahrenheit = celsius_to_fahrenheit(temperature_celsius)

    return f"Weather in {normalized_data['location']}: {temperature_celsius:.1f}°C ({temperature_fahrenheit:.1f}°F), humidity {normalized_data['humidity_percent']:.1f}%. Feels like: {feels_like:.1f}°C."
