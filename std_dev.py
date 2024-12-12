from random import randint
import statistics

def std_dev(data):
    e_x = sum(data) / len(data)
    sq_devs = [(value - e_x)**2 for value in data]
    std_dev = (sum(sq_devs) / (len(sq_devs) - 1))**0.5

    return std_dev

rand_data = [randint(1,100) for i in range(100)]

print("Homegrown Standard Deviation: " + str(std_dev(rand_data)))
print("Inbuilt Standard Deviation: " + str(statistics.stdev(rand_data)))
