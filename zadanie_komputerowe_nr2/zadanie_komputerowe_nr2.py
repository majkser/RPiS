import numpy as np
import random
import matplotlib.pyplot as plt

theroetical_pi_value = np.pi

trafienia = 0
strzaly = 10

strzaly_list = []
pi_list = []

while strzaly <= 100000:
    for i in range(strzaly):
        x = random.random()
        y = random.random()
        lentgh = np.sqrt(x**2 + y**2)
        if lentgh <= 1:
            trafienia += 1
        
        pi = 4 * (trafienia/strzaly)
        pi_list.append(pi)
        strzaly_list.append(strzaly)
        
    trafienia = 0
    
    print("wynik dla", strzaly, "strzalow:", f"{pi:.5f}")
    strzaly *= 10


plt.plot(strzaly_list, pi_list, color='purple', label='Prawdopodobieństwo trafienia w koło')
plt.axhline(y=theroetical_pi_value, color='red', linestyle='--', label='y1 = theoretical_pi_value')
plt.xlabel('Liczba strzałów')
plt.ylabel('Prawdopodobieństwo trafienia w koło')
plt.title('Zależność prawdopodobieństwa od liczby strzałów')
plt.xscale('log')
plt.legend()
plt.show()