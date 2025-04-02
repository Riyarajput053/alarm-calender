import requests

CLIENT_ID = "8a3b577b-32c2-4df4-868c-348d6ff347f8"
CLIENT_SECRET = "G6PyRDTFKyt3B6X1FbQKIDzwKylo3sUWpzakBQd2"

def get_access_token():
    url = "https://api.prokerala.com/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }
    response = requests.post(url, data=data)
    token_data = response.json()
    return token_data["access_token"]

access_token = get_access_token()
print("Access Token:", access_token)
