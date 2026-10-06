import requests

def test_api_estado():
    respuesta = requests.get("https://api.ejemplo.com/estado")
    assert respuesta.status_code == 200