from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import os
from datetime import datetime, timedelta
import time
import requests
from requests_toolbelt.utils import get_cookie_necessary

username = 'baptiste.barraque'
password = 'Applipluie12345*'
download_url = 'https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/466/M1_AVH13C1/2024/086/M1_AVH13C1.A2024086.006.2024088204133.nc'
filename = 'ndvitest.nc'


def download_file(url):
    login_url = "https://urs.earthdata.nasa.gov/home"

    # Données du formulaire de connexion
    login_data = {
        "username": "baptiste.barraque",
        "password": "Onepiece15*"
    }

# Envoyer la requête POST pour la connexion
    response = requests.post(login_url, data=login_data)

# Vérifier si la connexion a réussi
    if response.status_code == 200:
        # Extraire le jeton d'authentification ou les cookies de la réponse
        # (selon le mécanisme d'authentification du site Web)
        # Exemple : extraire le jeton d'un cookie nommé "auth"
        auth_cookie = get_cookie_necesary(response, 'auth')
        auth_token = auth_cookie.value

    # URL de la page de téléchargement

    # Inclure le jeton d'authentification dans l'en-tête de la requête de téléchargement
        headers = {
            "Authorization": "Bearer " + auth_token
        }

    # Envoyer la requête GET pour télécharger le fichier
        download_response = requests.get(url, headers=headers)

    # Vérifier si le téléchargement a réussi
        if download_response.status_code == 200:
            # Écrire le contenu du fichier téléchargé dans un fichier local
            with open("fichier_telecharge.nc", "wb") as f:
                f.write(download_response.content)
            print("Fichier téléchargé avec succès!")
        else:
            print(
                f"Erreur de téléchargement : {download_response.status_code}")
    else:
        print("Erreur de connexion : {response.status_code}")


download_file(download_url)
