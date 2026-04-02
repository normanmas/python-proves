# Exemple de Biaix i Variància

# Importar les llibreries
import numpy as np
import matplotlib.pyplot as plt

# Matriu de dades
punts = np.array([
    [1.0, 1.9],
    [1.5, 3.4],
    [2.0, 2.3],
    [2.5, 2.6],
    [3.0, 2.1],
    [3.5, 3.6],
    [4.0, 2.8],
    [5.0, 3.9],
    [6.0, 2.4],
    [6.5, 5.0],
    [7.0, 4.6]
    ])
print(punts)

# Separar les dades
x= punts[:,0]
y = punts[:,1]

# Crear el coeficients
coeficients_polinomi = np.polyfit(x, y, 10)
coeficients_recta = np.polyfit(x, y, 1)

p = np.poly1d(coeficients_polinomi)
r = np.poly1d(coeficients_recta)

xx = np.linspace(min(x), max(x), 500)
yy = p(xx)
yy_recta = r(xx)


print('Coeficients polinomi:')
print(coeficients_polinomi)
print('Coeficients recta:')
print(coeficients_recta)
print('Valors del polinomi:')
print(p(x))
plt.scatter(x, y, color="red", label="punts")
plt.plot(xx, yy, label="polinomi grau 10")
plt.legend()
plt.grid(True)
plt.show()
