# import numpy as np
from func import *

v = [42.0, 21.0, 31.0, 18.0, 27.0, 28.0, 48.0, 26.0, 28.0, 62.0, 56.0, 26.0, 18.0, 22.0, 26.0,
52.0, 16.0, 53.0, 20.0, 46.0, 48.0, 81.0, 38.0, 88.0, 86.0, 58.0, 49.0, 53.0, 18.0, 22.0, 60.0, 44.0, 60.0, 44.0,
71.0]

sortedV = sorted(v)
print(sortedV)
n = len(v)
print("n: ", n)

Xsr = find_Xsr(v)
print("Sredne vuborochnoe: ", Xsr)

S2 = find_Dispers(v, Xsr)
print("Dispersia: ", S2)

S = S2**(0.5)
print("Sr kv otklonenie: ", S)

V = 100*S/Xsr
print("coeff variacii", V)

Me = find_Median(v)
print("Mediana: ", Me)

ni = find_ni(v)

Mo = find_Moda(v, ni)
print("Moda: ", Mo)

Ex = find_Ex(v, ni, Xsr, S)
print("Excess: ", Ex)

As = find_As(v, ni, Xsr, S)
print("Assim: ", As)

poligon(v)
gistogramm(v)
empir(v)
