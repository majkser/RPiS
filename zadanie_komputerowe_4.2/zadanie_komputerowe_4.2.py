import numpy as np
import matplotlib.pyplot as plt

def functions(x):
    if x <= - 1 or x >= 3:
        return 0
    elif x > -1 and x <= 0:
        return 1/3 * x  + 1/3
    elif x > 0 and x <= 2:
        return 1/3
    elif x > 2 and x < 3:
        return -1/3 * x + 1
    
def generator (n):
    list = []
    
    while len(list) < n:
        x = np.random.uniform(-1, 3)
        y = np.random.uniform(0, 1/3)
        
        if y <= functions(x):
            list.append(x)
        
    return list

print(generator(1000))
