import pytest

from weather_sensor_sdk.detection.checks import (
    is_dict_sensor,
    is_string_sensor,
    is_tuple_list_sensor,
)


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
