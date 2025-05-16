import math

def generate_realization(random_num):
    x = -1 * math.log(1-random_num) / 12
    return x
