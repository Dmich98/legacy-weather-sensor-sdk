import pytest

from weather_sensor_sdk.normalization.converters import (
    normalize_dict_sensor,
    normalize_string_sensor,
    normalize_tuple_list_sensor,
    to_normalized_sensor,
)


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
