import pandas as pd

df = pd.read_excel("BBDD_MATRIZ_PP.xlsx", sheet_name=1)

def buscar(x):
    r = df.loc[
        df["DNI"] == x,
        ["DNI", "NOMBRE", "RAZON_SOCIAL", "NUMERO 1"]
    ]
    return r

print(buscar(44755659))