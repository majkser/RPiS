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

plt.figure(figsize=(12, 6))
for n_samples in [10**3, 10**5]:

    samples = generator(n_samples)
    
    x = np.linspace(-1, 3, 1000)
    y = [functions(xi) for xi in x]
    
    plt.hist(samples, bins=50, density=True, alpha=0.5, label=f'Histogram (n={n_samples})')

    plt.plot(x, y, 'r-', label='Teoretyczna FGP', linewidth=3)

    plt.title("Porównanie histogramu i teoretycznej funkcji gęstości")
    plt.xlabel("x")
    plt.ylabel("Gęstość prawdopodobieństwa")
    plt.legend()
    plt.grid(True)
    plt.show()
