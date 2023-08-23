import pandas as pd
import psycopg2

#Lecture du fichier csv

data = pd.read_csv("C:/Users/m_a_g/Desktop/cours/S2/Bussiness Database/Site Web/Etudiants_TP.csv", delimiter=";")
print("NB data: ", data.shape[0])

#Integration des donnes

print('Connexion à la BDD')
conn = psycopg2.connect(host = "localhost",
                        database = "ETUDIANTS",
                        user="postgres",
                        password="root")

print("Creation d'un curseur")
curseur = conn.cursor()

print("Intégration des données")
print(" > Truncate table")
curseur.execute('truncate table etudiants')
conn.commit()

print(" > Insertion des données")
for index, row in data.iterrows():
    taille = row[0]
    pointure = row[1]
    sexe = row[2]
    sql = "insert into etudiants (taille, pointure, sexe) values (%s,%s,%s)"
    record_to_insert = (taille, pointure, sexe)
    curseur.execute(sql, record_to_insert)
    conn.commit()

print(" > Vérification de l'insertion")
sql = "select count(1) from etudiants"
curseur.execute(sql)
res = curseur.fetchone()

print("NB données insérées: ", res[0],"/",data.shape[0])

conn.close()