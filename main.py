from format_weather import format_weather
from sensor import get_raw_data
from sensor_normalizer import normalize_sensor
from temperature_utils import calculate_feels_like


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
