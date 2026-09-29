from ..detection import detect_sensor_type
from ..models import SensorData, SensorType
from .converters import (
    normalize_dict_sensor,
    normalize_string_sensor,
    normalize_tuple_list_sensor,
)

NORMALIZERS = {
    SensorType.STRING: normalize_string_sensor,
    SensorType.DICT: normalize_dict_sensor,
    SensorType.TUPLE_LIST: normalize_tuple_list_sensor,
}


def normalize_sensor(data) -> SensorData:
    sensor_type = detect_sensor_type(data)

    return NORMALIZERS[sensor_type](data)
