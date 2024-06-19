import requests

# Paramètres de la requête
search_url = "https://cmr.earthdata.nasa.gov/search/granules/MOD13Q1"
params = {
    # Produit NDVI MODIS
    "temporal": "2023-01-01T00:00:00Z,2023-12-31T23:59:59Z",  # Plage de dates
    "page_size": 10,  # Nombre de résultats par page
    "page_num": 1,  # Numéro de page
    "token": "eyJ0eXAiOiJKV1QiLCJvcmlnaW4iOiJFYXJ0aGRhdGEgTG9naW4iLCJzaWciOiJlZGxqd3RwdWJrZXlfb3BzIiwiYWxnIjoiUlMyNTYifQ.eyJ0eXBlIjoiVXNlciIsInVpZCI6ImJhcHRpc3RlLmJhcnJhcXVlIiwiZXhwIjoxNzE1NTAzODIyLCJpYXQiOjE3MTAzMTk4MjIsImlzcyI6IkVhcnRoZGF0YSBMb2dpbiJ9.G1fM9-d8jHUtAgFSJfWrsLNWtW8uJJc51FqsFnmyytfdBAx-_Yw8_BCBnDBpwdC-8zS--HmKaIoyjORvLE9hiqmP-Tnq-KLuay2qh_v-_Bh1hPI0SlPiZpgaPkkM031kM7MS7nVjIpxY-5nlzlmYmDfnIyRtOZ6x2a8KAXHe9sXvJkh2_nIGs-HaSZ0g65ChDmFngodLJAcWb8p3Q0l7Ipu19oeiN22aQQSyjzUZracPsShpU-yG9wBBO0LiQu31nZmolWKD0B4iBmqa65BAm0lA5ByDv_JmFj5M2li1F8v8kl2fiWAKWEGmm8JhWGLhVL7WI0vqemWW3havk6kDwQ"  # Remplacez par votre jeton d'authentification Earthdata
}

# Faire la requête
response = requests.get(search_url, params=params)

# Vérifier le statut de la requête
if response.status_code == 200:
    # Vérifier si la réponse est au format JSON valide
    try:
        results = response.json()
        # Traiter les résultats...
        print(results)
    except ValueError:
        print("La réponse n'est pas au format JSON valide.")
else:
    print("Échec de la requête :", response.status_code)
