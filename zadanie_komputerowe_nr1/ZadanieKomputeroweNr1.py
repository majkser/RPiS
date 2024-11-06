import random
import matplotlib.pyplot as plt

zbior_kart = []
trefle = []
moc_zbioru_a = 0
moc_zbioru_omega = 0
prawdopodobienstwo = 0
licznik_eksperymentow = []
prawdopodobienstwa = []

while True:
    for i in range (3):
        wylosowana_karta = random.randint(1, 52)    
        
        while wylosowana_karta in zbior_kart:
            wylosowana_karta = random.randint(1, 52)

        zbior_kart.append(wylosowana_karta)
        
        if 1 <= wylosowana_karta <= 13:
            trefle.append(wylosowana_karta)
        
    if (len(trefle) == 0):
        moc_zbioru_a += 1
        moc_zbioru_omega += 1
    else:
        moc_zbioru_omega += 1
        
    trefle.clear()
    zbior_kart.clear()
    prawdopodobienstwo = moc_zbioru_a/moc_zbioru_omega
    licznik_eksperymentow.append(moc_zbioru_omega)
    prawdopodobienstwa.append(prawdopodobienstwo)

    
    if 0.413116 < prawdopodobienstwo < 0.413943:
        break

plt.figure(figsize=(12, 6))

plt.plot(licznik_eksperymentow, prawdopodobienstwa, color='purple', label='Prawdopodobieństwo')
plt.axhline(y=0.413116, color='red', linestyle='--', label='y1 = 0.413116')
plt.axhline(y=0.413943, color='green', linestyle='--', label='y2 = 0.413943')
plt.xlabel('Liczba eksperymentów')
plt.ylabel('Prawdopodobieństwo')
plt.title('Zależność prawdopodobieństwa od mocy zbioru Omega')
plt.legend()
plt.show()