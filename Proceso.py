import pandas as pd

df = pd.read_excel("BBDD_MATRIZ_PP.xlsx", sheet_name=1)
fd = pd.read_excel("CLIENTECAMPAÑA.xlsx")

def buscar(x):
        x = str(int(x))  # número → string

        if len(x) == 9:
            r = df.loc[
                df["NUMERO 1"].astype(str) == x,
                ["DNI", "NOMBRE", "RAZON_SOCIAL", "NUMERO 1"]
            ]
            return r

        elif len(x) == 8:
            r = df.loc[
                df["DNI"].astype(str) == x,
                ["DNI", "NOMBRE", "RAZON_SOCIAL", "NUMERO 1"]
            ]
            return r

        else:
            return "Número inválido"
def encontrar(y):
       
       z= df.loc[
                df["NumeroDocumento"]== y,
                ["Nombre", "MONTO","LIQUIDO","Tasa","Plazo","CuotaActual"]
            ]
       return z