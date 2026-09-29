from ..models import SensorData
from ..parsing import parse_humidity, parse_temperature, parse_wind_speed


def to_normalized_sensor(
    location: str,
    temperature_celsius: str | float,
    humidity_percent: str | int,
    wind_speed_mps: str | float,
) -> SensorData:
    return {
        "location": location.strip(),
        "temperature_celsius": parse_temperature(temperature_celsius),
        "humidity_percent": parse_humidity(humidity_percent),
        "wind_speed_mps": parse_wind_speed(wind_speed_mps),
    }


def normalize_string_sensor(data: str) -> SensorData:
    location, temperature, humidity, wind_speed = data.split(";")

    return to_normalized_sensor(
        location,
        temperature,
        humidity,
        wind_speed,
    )


def normalize_dict_sensor(data: dict) -> SensorData:
    weather = data.get("data", {})
    wind = weather.get("wind", {})

    return to_normalized_sensor(
        data.get("location", ""),
        weather.get("temperature", "0 C"),
        weather.get("humidity", "0%"),
        wind.get("speed", "0 m/s"),
    )


def normalize_tuple_list_sensor(data: list[tuple]) -> SensorData:
    data_dict = dict(data)

    return to_normalized_sensor(
        data_dict.get("city", ""),
        data_dict.get("temp_celsius", 0.0),
        data_dict.get("humidity_percent", 0),
        data_dict.get("wind_mps", 0.0),
    )
