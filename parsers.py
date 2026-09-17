def parse_temperature(value: str | float) -> float:
    if isinstance(value, str):
        value = value.removesuffix("C").strip()

    return float(value)


def parse_humidity(value: str | float) -> float:
    if isinstance(value, str):
        value = value.removesuffix("%").strip()

    return int(value)


def parse_wind_speed(value: str | float) -> float:
    if isinstance(value, str):
        value = value.removesuffix("m/s").strip()

    return float(value)
