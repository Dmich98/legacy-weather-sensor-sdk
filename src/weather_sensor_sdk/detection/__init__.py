"""Sensor input format recognition."""

from .checks import is_dict_sensor, is_string_sensor, is_tuple_list_sensor
from .detector import detect_sensor_type

__all__ = [
    "detect_sensor_type",
    "is_dict_sensor",
    "is_string_sensor",
    "is_tuple_list_sensor",
]
