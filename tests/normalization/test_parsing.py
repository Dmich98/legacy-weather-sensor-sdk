import pytest

from weather_sensor_sdk.parsing import (
    parse_humidity,
    parse_temperature,
    parse_wind_speed,
)


@pytest.mark.parametrize(
    "value, expected",
    [
        ("10.5C", 10.5),
        ("10.5 C", 10.5),
        ("-1.2C", -1.2),
        (14.2, 14.2),
    ],
)
def test_parse_temperature(value, expected):
    assert parse_temperature(value) == pytest.approx(expected)


@pytest.mark.parametrize(
    "value, expected",
    [
        ("78%", 78.0),
        ("85%", 85.0),
        (" 92% ", 92.0),
        (68.0, 68.0),
    ],
)
def test_parse_humidity(value, expected):
    assert parse_humidity(value) == pytest.approx(expected)


@pytest.mark.parametrize(
    "value, expected",
    [
        ("5.2m/s", 5.2),
        ("4.5 m/s", 4.5),
        (" 6.2 m/s ", 6.2),
        (3.9, 3.9),
    ],
)
def test_parse_wind_speed(value, expected):
    assert parse_wind_speed(value) == pytest.approx(expected)
