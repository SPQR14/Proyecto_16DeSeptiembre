import pandas as pd
o = 'r'
while o != 's':
    df = pd.read_csv("..\..\Data_set\Chispazo.csv", sep = ',', encoding='utf8')

    x1 = int(input("R1: "))
    x2 = int(input("R2: "))
    x3 = int(input("R3: "))
    x4 = int(input("R4: "))
    x5 = int(input("R5: "))

    if ( (df['R1'] == x1) &  (df['R2'] == x2) &(df['R3'] == x3) & (df['R4'] == x4) & (df['R5'] == x5) ).any():
        i_l = df[(df['R1'] == x1) &  (df['R2'] == x2) &(df['R3'] == x3) & (df['R4'] == x4) & (df['R5'] == x5)].index.tolist()
        print(f"Ya existe en el índice {i_l}")
        print(df.iloc[i_l])
    else:
        print("No existe")

    o = input("Presiona s para salir, cualquier otra tecla para continuar: ")