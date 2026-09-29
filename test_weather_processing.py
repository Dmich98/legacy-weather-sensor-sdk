import pytest

from parsers import parse_humidity, parse_temperature, parse_wind_speed
from sensor_checking import is_tuple_list_sensor
from sensor_converters import (
    normalize_dict_sensor,
    normalize_string_sensor,
    normalize_tuple_list_sensor,
    to_normalized_sensor,
)
from sensor_normalizer import normalize_sensor
from sensor_types import SensorType
from temperature_utils import calculate_feels_like, celsius_to_fahrenheit
from format_weather import format_weather


@pytest.mark.parametrize(
    "data, expected",
    [
        ("Kyiv;+10.5C;78%;5.2m/s", True),
        ("Lviv;-1.2C;92%;2.1m/s", True),
        ("Odesa;+15.0C;65%;7.8m/s", True),
        ("Kyiv;+10.5C;78%", False),
        ("", False),
        ("not-a-sensor", False),
        ({"location": "Kyiv"}, False),
        (123, False),
        (None, False),
    ],
)
def test_is_string_sensor(data, expected):
    from sensor_checking import is_string_sensor

    assert is_string_sensor(data) is expected


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            {
                "location": "Kharkiv",
                "data": {
                    "temperature": "5.1 C",
                    "humidity": "85%",
                    "wind": {
                        "speed": "4.5 m/s",
                        "direction": "NW",
                    },
                },
            },
            True,
        ),
        (
            {
                "location": "Dnipro",
                "data": {
                    "temperature": "7.8 C",
                    "humidity": "77%",
                    "wind": {
                        "speed": "3.9 m/s",
                        "direction": "S",
                    },
                },
            },
            True,
        ),
        ({}, False),
        ("Kyiv;+10.5C;78%;5.2m/s", False),
        (
            [
                ("city", "Zaporizhzhia"),
                ("temp_celsius", 9.3),
                ("humidity_percent", 79),
                ("wind_mps", 5.0),
            ],
            False,
        ),
        (123, False),
        (None, False),
    ],
)
def test_is_dict_sensor(data, expected):
    from sensor_checking import is_dict_sensor

    assert is_dict_sensor(data) is expected


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            [
                ("city", "Zaporizhzhia"),
                ("temp_celsius", 9.3),
                ("humidity_percent", 79),
                ("wind_mps", 5.0),
            ],
            True,
        ),
        (
            [
                ("city", "Mykolaiv"),
                ("temp_celsius", 14.2),
                ("humidity_percent", 68),
                ("wind_mps", 6.2),
            ],
            True,
        ),
        ("Kyiv;+10.5C;78%;5.2m/s", False),
        (
            {
                "location": "Kharkiv",
                "data": {
                    "temperature": "5.1 C",
                    "humidity": "85%",
                    "wind": {
                        "speed": "4.5 m/s",
                        "direction": "NW",
                    },
                },
            },
            False,
        ),
        ([], False),
        ([1, 2, 3], False),
        (123, False),
        (None, False),
    ],
)
def test_is_tuple_list_sensor(data, expected):

    assert is_tuple_list_sensor(data) is expected


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            "Kyiv;+10.5C;78%;5.2m/s",
            SensorType.STRING,
        ),
        (
            {
                "location": "Kharkiv",
                "data": {
                    "temperature": "5.1 C",
                    "humidity": "85%",
                    "wind": {
                        "speed": "4.5 m/s",
                        "direction": "NW",
                    },
                },
            },
            SensorType.DICT,
        ),
        (
            [
                ("city", "Zaporizhzhia"),
                ("temp_celsius", 9.3),
                ("humidity_percent", 79),
                ("wind_mps", 5.0),
            ],
            SensorType.TUPLE_LIST,
        ),
    ],
)
def test_detect_sensor_type(data, expected):
    from sensor_detector import detect_sensor_type

    assert detect_sensor_type(data) == expected


def test_detect_sensor_type_invalid():
    from sensor_detector import detect_sensor_type

    with pytest.raises(ValueError):
        detect_sensor_type("invalid-sensor-data")


@pytest.mark.parametrize(
    "location, temperature, humidity, wind_speed, expected",
    [
        (
            "Kyiv",
            "+10.5C",
            "78%",
            "5.2m/s",
            {
                "location": "Kyiv",
                "temperature_celsius": 10.5,
                "humidity_percent": 78,
                "wind_speed_mps": 5.2,
            },
        ),
        (
            " Lviv ",
            "-1.2 C",
            "92%",
            "2.1 m/s",
            {
                "location": "Lviv",
                "temperature_celsius": -1.2,
                "humidity_percent": 92,
                "wind_speed_mps": 2.1,
            },
        ),
    ],
)
def test_to_normalized_sensor(
    location,
    temperature,
    humidity,
    wind_speed,
    expected,
):
    result = to_normalized_sensor(
        location,
        temperature,
        humidity,
        wind_speed,
    )

    assert result == expected


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            "Kyiv;+10.5C;78%;5.2m/s",
            {
                "location": "Kyiv",
                "temperature_celsius": 10.5,
                "humidity_percent": 78,
                "wind_speed_mps": 5.2,
            },
        ),
        (
            "Lviv;-1.2C;92%;2.1m/s",
            {
                "location": "Lviv",
                "temperature_celsius": -1.2,
                "humidity_percent": 92,
                "wind_speed_mps": 2.1,
            },
        ),
    ],
)
def test_normalize_string_sensor(data, expected):
    assert normalize_string_sensor(data) == expected


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            {
                "location": "Kharkiv",
                "data": {
                    "temperature": "5.1 C",
                    "humidity": "85%",
                    "wind": {
                        "speed": "4.5 m/s",
                        "direction": "NW",
                    },
                },
            },
            {
                "location": "Kharkiv",
                "temperature_celsius": 5.1,
                "humidity_percent": 85,
                "wind_speed_mps": 4.5,
            },
        ),
        (
            {
                "location": "Dnipro",
                "data": {
                    "temperature": "7.8 C",
                    "humidity": "77%",
                    "wind": {
                        "speed": "3.9 m/s",
                        "direction": "S",
                    },
                },
            },
            {
                "location": "Dnipro",
                "temperature_celsius": 7.8,
                "humidity_percent": 77,
                "wind_speed_mps": 3.9,
            },
        ),
    ],
)
def test_normalize_dict_sensor(data, expected):
    assert normalize_dict_sensor(data) == expected


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            [
                ("city", "Zaporizhzhia"),
                ("temp_celsius", 9.3),
                ("humidity_percent", 79),
                ("wind_mps", 5.0),
            ],
            {
                "location": "Zaporizhzhia",
                "temperature_celsius": 9.3,
                "humidity_percent": 79,
                "wind_speed_mps": 5.0,
            },
        ),
        (
            [
                ("city", "Mykolaiv"),
                ("temp_celsius", 14.2),
                ("humidity_percent", 68),
                ("wind_mps", 6.2),
            ],
            {
                "location": "Mykolaiv",
                "temperature_celsius": 14.2,
                "humidity_percent": 68,
                "wind_speed_mps": 6.2,
            },
        ),
    ],
)
def test_normalize_tuple_list_sensor(data, expected):
    assert normalize_tuple_list_sensor(data) == expected


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            "Kyiv;+10.5C;78%;5.2m/s",
            {
                "location": "Kyiv",
                "temperature_celsius": 10.5,
                "humidity_percent": 78,
                "wind_speed_mps": 5.2,
            },
        ),
        (
            {
                "location": "Kharkiv",
                "data": {
                    "temperature": "5.1 C",
                    "humidity": "85%",
                    "wind": {
                        "speed": "4.5 m/s",
                        "direction": "NW",
                    },
                },
            },
            {
                "location": "Kharkiv",
                "temperature_celsius": 5.1,
                "humidity_percent": 85,
                "wind_speed_mps": 4.5,
            },
        ),
        (
            [
                ("city", "Zaporizhzhia"),
                ("temp_celsius", 9.3),
                ("humidity_percent", 79),
                ("wind_mps", 5.0),
            ],
            {
                "location": "Zaporizhzhia",
                "temperature_celsius": 9.3,
                "humidity_percent": 79,
                "wind_speed_mps": 5.0,
            },
        ),
    ],
)
def test_normalize_sensor(data, expected):
    assert normalize_sensor(data) == expected


def test_normalize_sensor_raises_error_for_unknown_format():
    with pytest.raises(ValueError):
        normalize_sensor(123)


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
