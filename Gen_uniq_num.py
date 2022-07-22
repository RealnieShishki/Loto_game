import random

def generate_unique_numbers(count, minbound, maxbound):
    if count > maxbound - minbound + 1:
        raise ValueError('Введены не правельные параметры')
    ret = []
    while len(ret) < count:
        new = random.randint(minbound, maxbound)
        if new not in ret:
            ret.append(new)
    return ret