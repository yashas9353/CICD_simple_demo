import pytest
from flask import Flask

# Import the app from your application file
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello(client):
    rv = client.get('/')
    assert b'Yashas Is The Best' in rv.data
