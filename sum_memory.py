# Так как до того как сроки сдачи вышли, пытался вычленить из locals() только мои переменные, решил взять тот вариант
# что вы показали на разборе и вставить тот самый "волшебный цикл".
# разрядность ОС 64
# интерпретатор CPython ('32bit', 'WindowsPE')
# Примеры для анализа взял не самые хорошие (из 5 задачи к 3му уроку), при одинаковом масиве для анализа все
# реализации занимают идентичное количество памяти 208 байт
# Зато когда массив генерировался random, объем варьируется в зависимости от того совпадают ли значения заданных
# вручную переменных со сгенерированными в масиве числами. Собственно это из-за того что в вашей реализации на
# которой основана моя, есть учет и сортировка уникальности посчитаных значений.
import sys


def sum_memory(objects):
    sum_mem = 0
    unique_id = set()
    for key, value in objects.items():
        if key.startswith('__'):
            continue
        elif hasattr(value, '__call__'):
            continue
        elif hasattr(value, '__loader__'):
            continue
        elif id(value) in unique_id:
            continue
        else:
            """
            к сожалению в моей реализации считается размер объектов только первой вложенности
            """
            if hasattr(value, '__iter__'):
                iter_sum = 0
                if hasattr(value, 'items'):
                    for k, v in value.items():
                        if id(k) not in unique_id:
                            unique_id.add(id(k))
                            sum_mem += sys.getsizeof(k)
                            iter_sum += sys.getsizeof(k)
                        else:
                            continue

                        if id(v) not in unique_id:
                            unique_id.add(id(v))
                            sum_mem += sys.getsizeof(v)
                            iter_sum += sys.getsizeof(v)
                        else:
                            continue

                elif not isinstance(value, str):
                    for item in value:
                        if id(item) not in unique_id:
                            unique_id.add(id(item))
                            sum_mem += sys.getsizeof(item)
                            iter_sum += sys.getsizeof(item)
                        else:
                            continue
                unique_id.add(id(value))
                sum_mem += sys.getsizeof(value)
                print(f'переменная {key} класса {type(value)} хранит итерируемый объект '
                      f'и включая размер объектов первой вложенности занимает {sys.getsizeof(value) + iter_sum} байт')
            else:
                unique_id.add(id(value))
                sum_mem += sys.getsizeof(value)
                print(f'переменная {key} класса {type(value)} хранит {value} '
                      f'и занимает {sys.getsizeof(value)} байт')

    return sum_mem
