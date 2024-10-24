import numpy as np
import random


trafienia = 0
strzaly = 10

while strzaly <= 100000:
    for i in range(strzaly):
        x = random.random()
        y = random.random()
        lentgh = np.sqrt(x**2 + y**2)
        if lentgh <= 1:
            trafienia += 1
        
        pi = 4 * (trafienia/strzaly)
        
    trafienia = 0
    
    print("wynik dla", strzaly, "strzalow:", f"{pi:.5f}")
    strzaly *= 10