from fastapi import FastAPI
from joblib import dump, load
import numpy as np

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello" : "World"}

@app.get("/estimation_pointure/{taille}")
async def estimation_pointure(taille:int):

    #Chargement du modele
    modele = load("C:/Users/m_a_g/Desktop/cours/S2/Bussiness Database/Site Web/reg_lineaire.mod")

    #Prediction
    X = [taille]
    X = np.array(X).reshape(-1,1)
    pointure = modele.predict(X)
    pointure = round(pointure[0],0)
    print("Taille recu : ", taille)
    print("Pointure prédite : ", pointure)

    print("Taille reçue : ", taille)
    return {"taille":taille, "pointure": pointure}