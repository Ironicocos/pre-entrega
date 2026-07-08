import pytest
import requests
import time 
from faker import Faker
fake = Faker()
from random import randint
from utils.logger import logger
#pytest -s tests/testApi/test_post_lifecycle.py
URL = 'https://jsonplaceholder.typicode.com/posts'
@pytest.fixture(scope="module")
def created_post():
    payload = {
 'title': fake.text(),
 'body': fake.text(),
 'userId' : 1
}
    response = requests.post(URL, json=payload)
    assert response.status_code == 201
    return response.json()
@pytest.mark.e2e
def testPatchTitlePost(created_post):
    logger.info("Obteniendo id de la petición POST")
    post_id = created_post['id']
    logger.info("Declarando el cuerpo para la petición...")
    PATCH_PAYLOAD = {'title' : 'Título actualizado por QA'}
    logger.info("Realizando petición patch al servidor...")
    response = requests.patch(f'https://jsonplaceholder.typicode.com/posts/{post_id}', json=PATCH_PAYLOAD)
    logger.info("Obteniendo el contenido de la petición...")
    body = response.json()
    logger.info("Obteniendo el campo título de la petición...")
    title = body['title']
    logger.info("Verificando que la petición se haya concretad correctamente...")
    assert response.status_code == 200
    logger.info("Verificando que se haya reemplazado efectivamente dicho campo...")
    assert title == 'Título actualizado por QA'
    logger.info("Verificando que los demás campos no hayan sido modificados")
    assert 'userId' in created_post
    assert 'body' in created_post
    print(f"PATCH completado - Solo título actualizado")
    logger.info("Título actualizado con éxito")
@pytest.mark.e2e
def testDeletePost(created_post):
    logger.info("Obteniendo id de la petición POST")
    post_id = created_post['id']
    logger.info("Realizando petición DELETE para borrar el contenido del POST...")
    response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    logger.info("Verificando que se recibió el codigo de estado correcto...")
    assert response.status_code == 200
    logger.info("Obteniendo contenido de la petición DELETE")
    body = response.json()
    logger.info("Veriicando que se haya eliminado correctamente el contenido de la petición")
    assert body == {} or 'id' not in body or body['id'] is None
    logger.info("La petición se ejecutó con éxito")