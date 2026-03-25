import pandas as pd

df = pd.read_excel("BBDD_GENERAL.xlsx")
fd = pd.read_excel("CLIENTECAMPAÑA.xlsx")

def buscar(x):
    x = str(x).strip()

    columnas = ["DNI", "NOMBRE", "RAZON_SOCIAL", "NUMERO 1", "NUMERO 2", "NUMERO 3"]

    if len(x) == 9:
        r = df.loc[
            df["NUMERO 1"].astype(str).str.strip() == x,
            columnas
        ]
        return r

    elif len(x) == 8:
        r = df.loc[
            df["DNI"].astype(str).str.strip() == x,
            columnas
        ]
        return r

    else:
        return pd.DataFrame(columns=columnas)
def encontrar(y):
       
       z= fd.loc[
                fd["NumeroDocumento"]== y,
                ["Nombre", "MONTO","LIQUIDO","Tasa","Plazo","CuotaActual","PLAZA"]
        
            ]
       return z
