import requests
import pytest
from utils.logger import logger
header = {
    'x-api-key': 'pub_9fefe6ac168ff0177c399f3c908ae0954798f5093f6332658e4f48e6480d0162'
    }
@pytest.mark.api
@pytest.mark.parametrize(
    "email, password",
    [
        ("eve.holt@reqres.in", "eve.holt@reqres.in"),
        ("cityslicka", " "),
        ],
)
def testSuccessfulLoginApi(email, password):
    logger.info("Asentando credenciales para el login...")
    body = {
        "email" : email,
        "password" : password
    }
    logger.info("Realizando la petición post...")
    response = requests.post('https://reqres.in/api/login', headers=header, json=body)
    logger.info("Verificando que se obtuvo el código de estado correcto...")
    assert response.status_code == 200, "No se pudo iniciar sesión correctamente"
    logger.info("Verificando que toquen se encuentra en el cuerpo de la petición...")
    assert 'token' in response.json()
@pytest.mark.api
@pytest.mark.parametrize(
    "email, password",
    [
        ("eve.holt@reqres.in", "eve.holt@reqres.in"),
        ("cityslicka", " "),
        ],
)
def testFailedLoginApi(email, password):
    logger.info("Asentando credenciales para el login...")
    body = {
        "email" : email,
        "password" : password
    }
    logger.info("Realizando la petición post...")
    response = requests.post('https://reqres.in/api/login', headers=header, json=body)
    logger.info("Verificando que se obtuvo el código de estado correcto...")
    assert response.status_code == 400, "Se esperaba un campo vacio"