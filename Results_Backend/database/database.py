from pymongo import MongoClient
import json
import certifi

ca = certifi.where()

######################################
#   CARGA ARCHIVOS CONFIGURACION     #
######################################
def loadConfigFile():
    with open(r'C:\Users\ANDRES\Documents\8. PROJECT\Registraduria\Results_Backend\database\config.json') as f:
        data = json.load(f)
    return data

######################################
#       FUNCION DE CONEXION          #
######################################
def dbConnection():
    dataConfig = loadConfigFile()
    try:
        client = MongoClient(dataConfig['MONGO_URI_SERVER'], tlsCAFile = ca)
        #client = MongoClient(dataConfig['MONGO_URI_LOCAL'], dataConfig['LOCAL_PORT'])
        db = client["Registraduria_Backend"]
    except ConnectionError:
        print("Error de conexión con la db")
    return db
    