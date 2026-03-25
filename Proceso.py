import pandas as pd

df = pd.read_excel("BBDD_GENERAL.xlsx")
fd = pd.read_excel("CLIENTECAMPAÑA.xlsx")

def buscar(x):
       
        x = str(int(x))
          
        if len(x) == 9:
            r = df.loc[
                df["NUMERO 1"].astype(str).str.strip() == x ,
                ["DNI", "NOMBRE", "RAZON_SOCIAL", "NUMERO 1","NUMERO 2","NUMERO 3"]
            ]
            return r

        elif len(x) == 8:
            r = df.loc[
                df["DNI"].astype(str) == x,
                ["DNI", "NOMBRE", "RAZON_SOCIAL", "NUMERO 1","NUMERO 2","NUMERO 3"]
            ]
            return r

        else:
            return st.warning(f"NO SE ECNONTRO{x}")
def encontrar(y):
       
       z= fd.loc[
                fd["NumeroDocumento"]== y,
                ["Nombre", "MONTO","LIQUIDO","Tasa","Plazo","CuotaActual","PLAZA"]
        
            ]
       return z
