import pytest

from weather_sensor_sdk.formatting import format_weather


@pytest.mark.parametrize(
    "normalized_data, feels_like, expected",
    [
        (
            {
                "location": "Kyiv",
                "temperature_celsius": 10.5,
                "humidity_percent": 78.0,
                "wind_speed_mps": 5.2,
            },
            10.8,
            "Weather in Kyiv: 10.5°C (50.9°F), humidity 78.0%. Feels like: 10.8°C.",
        ),
        (
            {
                "location": "Lviv",
                "temperature_celsius": -1.2,
                "humidity_percent": 92.0,
                "wind_speed_mps": 2.1,
            },
            -3.4,
            "Weather in Lviv: -1.2°C (29.8°F), humidity 92.0%. Feels like: -3.4°C.",
        ),
    ],
)
def test_format_weather(normalized_data, feels_like, expected):
    assert format_weather(normalized_data, feels_like) == expected
