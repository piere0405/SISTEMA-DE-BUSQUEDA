import pandas as pd

df = pd.read_excel("BBDD_GENERAL.xlsx")
fd = pd.read_excel("CLIENTECAMPAÑA.xlsx")

def buscar(x):
    x = str(x).strip()

    columnas = ["DNI", "NOMBRE", "RAZON_SOCIAL", "NUMERO 1", "NUMERO 2", "NUMERO 3"]

 
    df["NUMERO 1"] = df["NUMERO 1"].astype(str).str.replace(".0", "", regex=False).str.strip()
    df["NUMERO 2"] = df["NUMERO 2"].astype(str).str.replace(".0", "", regex=False).str.strip()
    df["NUMERO 3"] = df["NUMERO 3"].astype(str).str.replace(".0", "", regex=False).str.strip()
    df["DNI"] = df["DNI"].astype(str).str.strip()

    if len(x) == 9:
        mask = (
            (df["NUMERO 1"] == x) |
            (df["NUMERO 2"] == x) |
            (df["NUMERO 3"] == x)
        )
        return df.loc[mask, columnas]

    elif len(x) == 8:
        return df.loc[df["DNI"] == x, columnas]

    else:
        return pd.DataFrame(columns=columnas)
def encontrar(y):
       
       z= fd.loc[
                fd["NumeroDocumento"]== y,
                ["Nombre", "MONTO","LIQUIDO","Tasa","Plazo","CuotaActual","PLAZA","NUMERO_PRINCIPAL"]
        
            ]
       return z
