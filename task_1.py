# Определение количества различных подстрок с использованием хеш-функции
from hashlib import sha256


def substring_count2(_str):
    substring_counter = []
    for i in range(len(_str)):
        for j in range(1, len(_str)):
            if i + j <= len(_str):
                if sha256(bytes(_str[i: (i + j)], encoding='utf-8')).hexdigest() not in substring_counter:
                    substring_counter.append(sha256(bytes(_str[i: (i + j)], encoding='utf-8')).hexdigest())
    return len(substring_counter)


print(substring_count2('papa'))
print(substring_count2('sova'))

