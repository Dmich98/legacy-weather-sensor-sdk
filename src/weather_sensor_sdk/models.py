from enum import StrEnum
from typing import TypedDict


class SensorType(StrEnum):
    STRING = "string"
    DICT = "dict"
    TUPLE_LIST = "tuple_list"


class SensorData(TypedDict):
    location: str
    temperature_celsius: float
    humidity_percent: float
    wind_speed_mps: float
