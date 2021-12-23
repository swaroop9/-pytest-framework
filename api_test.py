import pytest
import requests
import json


@pytest.fixture
def getUrl():
    return 'https://reqres.in/'


def test_valid_login(getUrl):
    url = getUrl + 'api/login'
    data = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
        }

    response = requests.post(url, data=data)
    assert response.status_code == 200
    res_json = json.loads(response.text)
    assert res_json['token'] == 'QpwL5tke4Pnpja7X4'