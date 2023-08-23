#Modelisation

import psycopg2
import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score
from joblib import dump, load

print('Connexion à la BDD')
conn = psycopg2.connect(host = "localhost", 
                        database = "ETUDIANTS", 
                        user="postgres",
                        password = "root")

print("Creation d'un curseur")
curseur = conn.cursor()

print("Récupération des données")
X = []
Y = []

sql = "Select taille, pointure from etudiants where sexe = 'M'"
curseur.execute(sql)
res = curseur.fetchall()

for observation in res:
    X.append(float(observation[0]))
    Y.append(float(observation[1]))

conn.close()

print("Modélisation")

X_train = np.array(X).reshape(-1,1)
Y_train = np.array(Y)
modele = linear_model.LinearRegression()
modele.fit(X_train,Y_train)

y_pred = modele.predict(X_train)
print(y_pred)
R2 = r2_score(Y_train,y_pred)
beta0 = modele.intercept_
beta1 = modele.coef_[0]
print("B0: ", beta0, " --   B1: ",beta1)
print("R2 score : ", R2)

print(" > Sauvegarde du modèle")
dump(modele, 'C:/Users/m_a_g/Desktop/cours/S2/Bussiness Database/Site Web/reg_lineaire.mod')