import math


class number_generator:

    def __init__(self):
        self.curr_x = 1000

    def get_random_number(self):
        new_x = (24693*self.curr_x +3517)%math.pow(2, 17)
        self.curr_x = new_x
        return self.curr_x/math.pow(2,17)

num_gen = number_generator()
for i in range(1000):
    print(num_gen.get_random_number())
    
