import pandas as pd
import numpy as np

df = pd.read_csv("..\..\Data_set\Chispazo.csv", sep = ',', encoding='utf8')

v1 = list(df['R1'])
v2 = list(df['R2'])
v3 = list(df['R3'])
v4 = list(df['R4'])
v5 = list(df['R5'])

def matriz_de_transicion(transiciones):
    n =  max(transiciones) + 1
    M =[[0]*n for _ in range(n)]
    for (i,j) in zip(transiciones, transiciones[1:]):
        M[i][j] += 1
    for r in M:
        s = sum(r)
        if s > 0:
            r[:] = [f/s for f in r]
    return M

m1 = np.multiply(np.asmatrix(matriz_de_transicion(v1)).transpose(), 100.0)
m2 = np.multiply(np.asmatrix(matriz_de_transicion(v2)).transpose(), 100.0)
m3 = np.multiply(np.asmatrix(matriz_de_transicion(v3)).transpose(), 100.0)
m4 = np.multiply(np.asmatrix(matriz_de_transicion(v4)).transpose(), 100.0)
m5 = np.multiply(np.asmatrix(matriz_de_transicion(v5)).transpose(), 100.0)

def pasar_a_csv(m, x):
    df = pd.DataFrame(m)
    df.to_csv(f"..\..\Data_set\m{x}.csv", index = False, sep = ',', encoding = 'utf8')


pasar_a_csv(m1, 1)
pasar_a_csv(m2, 2)
pasar_a_csv(m3, 3)
pasar_a_csv(m4, 4)
pasar_a_csv(m5, 5)




