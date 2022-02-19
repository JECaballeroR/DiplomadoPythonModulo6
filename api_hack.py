import subprocess
import requests

api_port = 8000
api_url = f"http://0.0.0.0:{api_port}"

try:
    r = requests.get(api_url)
    if r.ok:
        print("La API ya esta corriendo :)")
except requests.exceptions.ConnectionError:
    print("Inicializando la API...")
    cmd = ["uvicorn", "api:app"]
    subprocess.Popen(cmd, close_fds=True)


def _prepare_data(self):
'''
Clase de preparar lo datos.
Este método convierte las entradas en los datos que tenían en X_train y X_test.

Miren el orden de las columnas de los datos antes de su modelo.
Tienen que recrear ese orden, en un dataframe de una fila.

'''
# Pueden manejar así las variables categoricas.
# Revisen los X!!! De eso depende que valores hay aquí.
# Para ver más o menos que valores pueden ser, en un data frame se le aplico pd.get_dummies, corran algo como:
# X_test[[col for col in X_test.columns if "nombre de columna" in col]].drop_duplicates()

catM = self.Marca
catC = self.Clase
catF = self.Fechas

list(X_train.columns)


df= pd.DataFrame(columns=list(X_train.columns),
data=[[*[0]*len(list(X_train.columns))]])

df['Marca']=self.Marca
df['Clase']=self.Clase


df2 = X_train.iloc[:0,:]
df3 = pd.DataFrame(columns=df2.columns, data=[[*[0]*len(df2.columns)]])

columM = [x for x in df3.columns if "Marca_" in x and str(catM)== x.split('_')[-1]]
df3[columM] = 1
columC = [x for x in df3.columns if "Clase_" in x and str(catC)== x.split('_')[-1]]
df3[columC] = 1
columF = [x for x in df3.columns if "Fechas_" in x and str(catF)== x.split('_')[-1]]
df3[columF] = 1
# Hacemos el DataFrame.
# Ponemos en columns lo que nos da de correr list(X_test.columns)
# En data, ponemos los datos en el orden en que están en las columnas

df4 = pd.DataFrame(columns=df3.columns,
data=[
[self.IdServicio,self.Bcpp,self.Potencia,self.Cilindraje,
self.PesoCategoria,df3[columM],df3[columC],df3[columF]]])

return df4