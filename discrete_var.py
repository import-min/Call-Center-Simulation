

def generate_realization(random_num):
    CDF = [.2, .5, 1]
    for num in range(len(CDF)):
        if CDF[num] > random_num:
            return num
    return len(CDF)
