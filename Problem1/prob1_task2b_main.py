import random
import numpy as np

N = 1000  # random walk steps
repeats = 10000
rval = np.zeros(repeats)
for l in range(repeats):
    random.seed(4397 + l)
    y = 0
    x = 0
    for i in range(N):
        rand = random.random()
        if rand < 0.25:
            y = y + 1
        elif rand < 0.5:
            y = y - 1
        elif rand < 0.75:
            x = x + 1
        else:
            x = x - 1
    rval[l] = y ** 2 + x ** 2
print(np.average(rval))
