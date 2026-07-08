import requests
import pytest
from utils.logger import logger
#pytest -s tests/testCreateUserApi.py
header = {
    'x-api-key': 'pub_9fefe6ac168ff0177c399f3c908ae0954798f5093f6332658e4f48e6480d0162'
    }
@pytest.mark.api
@pytest.mark.parametrize("body", [
    {  
    'first_name' : "Thiago",
    'last_name' : 'Guinazu',
    'job' : 'unemployed'
    },
    {
        'first_name' : 'Mauricio',
        'last_name' : 'Torres',
        'job' : 'employed',
    }
])
def testCreateUser(body):
    logger.info("Realizando petición de tipo POST...")
    response = requests.post("https://reqres.in/api/users", headers = header, json = body)
    logger.info("Verificando recibir el código de estado correcto...")
    assert response.status_code == 201
    logger.info("Obteniendo el contenido de la petición...")
    newUser = response.json()
    logger.info("Verificando si la fecha es correcta...")
    assert "2026" in newUser['createdAt']
    logger.info("Petición concretada con éxito")

    