import requests
import pytest
from utils.logger import logger
#pytest -s tests/testApi/testUsersApi.py
header = {
    'x-api-key': 'pub_9fefe6ac168ff0177c399f3c908ae0954798f5093f6332658e4f48e6480d0162'
    }
@pytest.mark.api
def testUserInfo():
    logger.info("Realizando petición tipo GET")
    response = requests.get("https://reqres.in/api/users?page=1", headers = header)
    logger.info("Verificando petición satisfactoria...")
    assert response.status_code == 200
    logger.info("Obteniendo los datos del encabezado en la petición...")
    body = response.json()
    logger.info("Obteniendo los datos del diccionario dentro del encabezado...")
    data = body['data']
    logger.info("Verificando que los datos sean correctos...")
    for user in data:
        assert user['avatar'].endswith('.jpg'), "El formato del avatar no es el solicitado"
        for i in ['id', 'first_name', 'email', 'last_name']:
            assert i in user
    logger.info("Los datos solicitados son correctos")