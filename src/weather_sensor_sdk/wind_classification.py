from bisect import bisect_left
from enum import StrEnum
from math import inf

from .models import WindSpeedMps


class WindCategory(StrEnum):
    CALM = "Calm"
    LIGHT_AIR = "Light air"
    LIGHT_BREEZE = "Light breeze"
    GENTLE_BREEZE = "Gentle breeze"
    MODERATE_BREEZE = "Moderate breeze"
    FRESH_BREEZE = "Fresh breeze"
    STRONG_WIND_WARNING = "Strong wind (warning)"


_WIND_CATEGORIES = (
    (0.2, WindCategory.CALM),
    (1.5, WindCategory.LIGHT_AIR),
    (3.3, WindCategory.LIGHT_BREEZE),
    (5.4, WindCategory.GENTLE_BREEZE),
    (7.9, WindCategory.MODERATE_BREEZE),
    (10.7, WindCategory.FRESH_BREEZE),
    (inf, WindCategory.STRONG_WIND_WARNING),
)


def classify_wind_speed(wind_speed: WindSpeedMps) -> WindCategory:
    index = bisect_left(
        _WIND_CATEGORIES,
        wind_speed,
        key=lambda item: item[0],
    )
    return _WIND_CATEGORIES[index][1]
