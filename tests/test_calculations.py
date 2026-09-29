import pytest

from weather_sensor_sdk.calculation import (
    calculate_feels_like,
    celsius_to_fahrenheit,
)


@pytest.mark.parametrize(
    "celsius, expected",
    [
        (0.0, 32.0),
        (10.0, 50.0),
        (37.0, 98.6),
        (100.0, 212.0),
        (-40.0, -40.0),
        (-10.0, 14.0),
        (10.5, 50.9),
    ],
)
def test_celsius_to_fahrenheit(celsius: float, expected: float):
    assert celsius_to_fahrenheit(celsius) == pytest.approx(expected)


@pytest.mark.parametrize(
    "temperature, humidity, wind_speed, expected",
    [(10.5, 78.0, 5.2, 6.12), (5.1, 85.0, 4.5, 0.41), (14.2, 68.0, 6.2, 9.49)],
)
def test_calculate_feels_like(
    temperature: float,
    humidity: float,
    wind_speed: float,
    expected: float,
):
    result = calculate_feels_like(
        temperature,
        humidity,
        wind_speed,
    )

    assert result == pytest.approx(expected, abs=0.01)
