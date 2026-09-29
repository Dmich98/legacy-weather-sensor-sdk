from weather_sensor_sdk.calculation import calculate_feels_like
from weather_sensor_sdk.formatting import format_weather
from weather_sensor_sdk.normalization import normalize_sensor
from mocks.sensor_api import get_raw_data


def main() -> None:
    raw_sensor_data = get_raw_data()

    print(f"Raw sensor data: {raw_sensor_data}")

    normalized_sensor_data = normalize_sensor(raw_sensor_data)

    feels_like_temperature = calculate_feels_like(
        normalized_sensor_data["temperature_celsius"],
        normalized_sensor_data["humidity_percent"],
        normalized_sensor_data["wind_speed_mps"],
    )

    formatted_weather = format_weather(normalized_sensor_data, feels_like_temperature)

    print(f"\nFormatted weather:\n{formatted_weather}")


if __name__ == "__main__":
    main()
