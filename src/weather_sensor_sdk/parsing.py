from .models import WindSpeedMps


def _parse_value(value: str | float, suffix: str) -> float:
    if isinstance(value, str):
        value = value.strip().removesuffix(suffix).strip()

    return float(value)


def parse_temperature(value: str | float) -> float:
    return _parse_value(value, "C")


def parse_humidity(value: str | float) -> float:
    return _parse_value(value, "%")


def parse_wind_speed(value: str | float) -> WindSpeedMps:
    parsed_value = _parse_value(value, "m/s")
    return WindSpeedMps(parsed_value)
