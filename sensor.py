import random


_MOCK_DATA = [
    # Формат 1: Рядок
    "Kyiv;+10.5C;78%;5.2m/s",
    "Lviv;-1.2C;92%;2.1m/s",
    "Odesa;+15.0C;65%;7.8m/s",

    # Формат 2: Словник
    {
        'location': 'Kharkiv',
        'data': {
            'temperature': '5.1 C',
            'humidity': '85%',
            'wind': {
                'speed': '4.5 m/s',
                'direction': 'NW'  # Додаткове поле, яке студенти мають ігнорувати
            }
        }
    },
    {
        'location': 'Dnipro',
        'data': {
            'temperature': '7.8 C',
            'humidity': '77%',
            'wind': {
                'speed': '3.9 m/s',
                'direction': 'S'
            }
        }
    },

    # Формат 3: Список кортежів
    [
        ('city', 'Zaporizhzhia'),
        ('temp_celsius', 9.3),
        ('humidity_percent', 79),
        ('wind_mps', 5.0)
    ],
    [
        ('city', 'Mykolaiv'),
        ('temp_celsius', 14.2),
        ('humidity_percent', 68),
        ('wind_mps', 6.2)
    ]
]


def get_raw_data():
    return random.choice(_MOCK_DATA)


if __name__ == '__main__':
    print("Демонстрація роботи модуля sensor.py")
    print("="*40)
    for i in range(5):
        print(f"Виклик #{i+1}:")
        raw_data = get_raw_data()
        print(f"  Тип даних: {type(raw_data)}")
        print(f"  Отримані дані: {raw_data}\n")
