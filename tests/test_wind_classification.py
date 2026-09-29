import pytest
from weather_sensor_sdk.models import WindSpeedMps
from weather_sensor_sdk.wind_classification import WindCategory, classify_wind_speed


@pytest.mark.parametrize(
    "wind_speed, expected",
    [
        (WindSpeedMps(0.0), WindCategory.CALM),
        (WindSpeedMps(0.2), WindCategory.CALM),
        (WindSpeedMps(1.5), WindCategory.LIGHT_AIR),
        (WindSpeedMps(3.3), WindCategory.LIGHT_BREEZE),
        (WindSpeedMps(5.4), WindCategory.GENTLE_BREEZE),
        (WindSpeedMps(7.9), WindCategory.MODERATE_BREEZE),
        (WindSpeedMps(10.7), WindCategory.FRESH_BREEZE),
        (WindSpeedMps(10.8), WindCategory.STRONG_WIND_WARNING),
        (WindSpeedMps(15.0), WindCategory.STRONG_WIND_WARNING),
        (WindSpeedMps(40.0), WindCategory.STRONG_WIND_WARNING),
    ],
    ids=[
        "is_calm_wind",
        "is_calm_wind_upper_bound",
        "is_light_air_wind",
        "is_light_breeze_wind",
        "is_gentle_breeze_wind",
        "is_moderate_breeze_wind",
        "is_fresh_breeze_wind",
        "is_strong_wind_warning",
        "is_strong_wind_upper_bound",
        "is_strong_wind_warning_far_above_upper_bound",
    ],
)
def test_classify_wind_speed(wind_speed, expected):

    assert classify_wind_speed(wind_speed) == expected
