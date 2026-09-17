import math

_FAHRENHEIT_SCALE_FACTOR = 9 / 5
_FAHRENHEIT_ZERO_OFFSET = 32


_VAPOR_PRESSURE_COEFFICIENT = 6.105
_VAPOR_PRESSURE_EXPONENT = 17.27
_VAPOR_PRESSURE_OFFSET = 237.7

_HUMIDITY_FACTOR = 0.33
_WIND_FACTOR = 0.70
_APPARENT_TEMPERATURE_OFFSET = 4.0


def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * _FAHRENHEIT_SCALE_FACTOR + _FAHRENHEIT_ZERO_OFFSET


def calculate_feels_like(
    temperature: float,
    humidity: float,
    wind_speed: float,
) -> float:
    humidity_ratio = humidity / 100

    exponent = (
        _VAPOR_PRESSURE_EXPONENT * temperature / (_VAPOR_PRESSURE_OFFSET + temperature)
    )

    vapor_pressure = humidity_ratio * _VAPOR_PRESSURE_COEFFICIENT * math.exp(exponent)

    humidity_effect = _HUMIDITY_FACTOR * vapor_pressure
    wind_effect = _WIND_FACTOR * wind_speed

    return temperature + humidity_effect - wind_effect - _APPARENT_TEMPERATURE_OFFSET
