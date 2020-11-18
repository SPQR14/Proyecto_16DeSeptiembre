import pandas as pd 
df = pd.read_csv("D:\Desarrollo\Proyecto_16DeSeptiembre\Data_set\Chispazo.csv", sep = ',', encoding='utf8')

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

m1 = matriz_de_transicion(v1)

m2 = matriz_de_transicion(v2)

m3 = matriz_de_transicion(v3)

m4 = matriz_de_transicion(v4)

m5 = matriz_de_transicion(v5)

def pasar_a_csv(m, x):
    df = pd.DataFrame(m)
    df.to_csv(f"D:\Desarrollo\Proyecto_16DeSeptiembre\Data_set\m{x}.csv", index = False, sep = ',', encoding = 'utf8')

pasar_a_csv(m1, 1)
pasar_a_csv(m2, 2)
pasar_a_csv(m3, 3)
pasar_a_csv(m4, 4)
pasar_a_csv(m5, 5)





