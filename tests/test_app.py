import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """1. Testa a página inicial"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, World!' in response.data

def test_about_page(client):
    """2. Testa a página /about"""
    response = client.get('/about')
    assert response.status_code == 200
    assert b'Sobre este projeto' in response.data

def test_api_get_message(client):
    """3. Testa o GET da API"""
    response = client.get('/api/message')
    json_data = response.get_json()
    assert response.status_code == 200
    assert 'message' in json_data
    assert json_data['message'] == 'Hello, World!'

def test_api_post_message(client):
    """4. Testa o POST na API"""
    response = client.post('/api/message', json={'message': 'Nova mensagem'})
    json_data = response.get_json()
    assert response.status_code == 201
    assert json_data['new_message'] == 'Nova mensagem'

def test_api_post_and_get_flow(client):
    """5. Testa fluxo: POST seguida de GET"""
    post_response = client.post('/api/message', json={'message': 'Mensagem Teste Fluxo'})
    assert post_response.status_code == 201
    
    get_response = client.get('/api/message')
    json_data = get_response.get_json()
    assert get_response.status_code == 200
    assert json_data['message'] == 'Mensagem Teste Fluxo'
