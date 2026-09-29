import pytest

from weather_sensor_sdk.detection import detect_sensor_type
from weather_sensor_sdk.models import SensorType


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

    assert detect_sensor_type(data) == expected


def test_detect_sensor_type_invalid():

    with pytest.raises(ValueError):
        detect_sensor_type("invalid-sensor-data")
