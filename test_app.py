import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {'status': 'ok', 'service': 'calculator-api'}

def test_add_route(client):
    response = client.get('/add/10/5')
    assert response.status_code == 200
    assert response.json == {'result': 15}

def test_subtract_route(client):
    response = client.get('/subtract/10/5')
    assert response.status_code == 200
    assert response.json == {'result': 5}

def test_multiply_route(client):
    response = client.get('/multiply/10/5')
    assert response.status_code == 200
    assert response.json == {'result': 50}

def test_divide_route(client):
    response = client.get('/divide/10/5')
    assert response.status_code == 200
    assert response.json == {'result': 2.0}

def test_divide_by_zero_route(client):
    response = client.get('/divide/10/0')
    assert response.status_code == 400
    assert response.json == {'error': 'Cannot divide by zero'}
