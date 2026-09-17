def is_string_sensor(data) -> bool:
    if not isinstance(data, str):
        return False

    # Four fields are the stable structural marker of the legacy string format.
    parts = data.split(";")

    return len(parts) == 4


def is_dict_sensor(data) -> bool:
    return isinstance(data, dict)


def is_tuple_list_sensor(data) -> bool:
    # The third legacy format encodes every field as a key-value tuple.
    return isinstance(data, list) and all(isinstance(item, tuple) for item in data)
