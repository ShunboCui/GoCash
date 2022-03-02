import os
import tempfile
import pytest
from app import app
from flask import Flask

# Initialize
#------------------------------------------------
@pytest.fixture
def client(request):
    test_client = app.test_client()
    def teardown():
        pass
    request.addfinalizer(teardown)
    return test_client
#-----------------------------------------------

def test_dummy(client):
    url='/api/dummy'
    response = client.get(url)
    assert (response.status_code == 200) and type(response.data) is not None