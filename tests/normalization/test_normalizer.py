import pytest

from weather_sensor_sdk.normalization import normalize_sensor


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
