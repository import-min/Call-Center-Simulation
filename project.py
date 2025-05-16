import math
import statistics
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class number_generator:

    def __init__(self):
        self.curr_x = 1000

    def get_random_number(self):
        new_x = (24693 * self.curr_x + 3517) % math.pow(2, 17)
        self.curr_x = new_x
        return self.curr_x / math.pow(2, 17)

def generate_discrete_realization(random_num):
    CDF = [0.2, 0.5, 1]
    for num in range(len(CDF)):
        if CDF[num] > random_num:
            return num

def generate_continuous_realization(random_num):
    return -12 * math.log(1 - random_num)

num_gen = number_generator()


W_realizations = []


for _ in range(500):
    total_time = 0
    unsuccessful_calls = 0

    while unsuccessful_calls < 4:
        # availability
        availability = generate_discrete_realization(num_gen.get_random_number())

        

        if availability == 2:  # available
            time_X = generate_continuous_realization(num_gen.get_random_number())

            if  time_X < 25:
                total_time += 6 + time_X 
                break
            else:
                # representative hangs up
                total_time += 6 + 25 + 1
                unsuccessful_calls += 1

        elif availability == 1:    # unavailable
            total_time += 6 + 25 + 1
            unsuccessful_calls += 1
            
        else: # busy
            total_time += 6 + 3 + 1
            unsuccessful_calls += 1
            

    W_realizations.append(total_time)


W_realizations = sorted(W_realizations)
mean_W = sum(W_realizations) / len(W_realizations)
median_W = statistics.median(W_realizations)

df = pd.DataFrame(W_realizations, columns=["realizations"])

#print(sorted(W_realizations))
#print(df.describe())
#print(statistics.quantiles(W_realizations, method='inclusive'))

print("Mean:", mean_W)
print("Median:", median_W)
print("First Quartile:", np.percentile(W_realizations, 25))
print("Third Quartile:", np.percentile(W_realizations, 75))

x = []
y = []
first = True
for i in (W_realizations):
    if (first):
        x.append(1/500)
        first = False
    else:
        x.append(x[-1] + 1/500)
    y.append(i)

plt.plot(y,x)
plt.xlabel('Time calling customer')
plt.ylabel('Probability of value or less')
plt.title("CDF of 500 realizations of calling customers")
plt.show()