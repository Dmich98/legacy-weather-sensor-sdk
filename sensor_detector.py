from sensor_checking import (
    is_dict_sensor,
    is_string_sensor,
    is_tuple_list_sensor,
)
from sensor_types import SensorType

SENSOR_TYPE_CHECKS = {
    is_string_sensor: SensorType.STRING,
    is_dict_sensor: SensorType.DICT,
    is_tuple_list_sensor: SensorType.TUPLE_LIST,
}


def detect_sensor_type(data) -> SensorType:
    for check, sensor_type in SENSOR_TYPE_CHECKS.items():
        if check(data):
            return sensor_type

    raise ValueError(f"Unknown sensor data format: {data}")
