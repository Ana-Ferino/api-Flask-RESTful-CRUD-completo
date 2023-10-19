
def test_login_successfully(test_client):
    status = 200
    response = test_client.post("/login/", headers={"Content-Type": "application/json"}, json={"Auth":{"usuario": "valid_user", "senha": "valid_password"}})
    assert response.status_code == status


def test_try_to_login_with_wrong_user_credentials(test_client):
    status = 401
    response = test_client.post("/login/", headers={"Content-Type": "application/json"}, json={"Auth":{"usuario": "valid_user", "senha": "invalid_password"}})
    assert response.status_code == status


def test_try_to_login_with_invalid_payload(test_client):
    status = 420
    response = test_client.post("/login/", headers={"Content-Type": "application/json"}, json={"Auth":{"payload_invalido"}})
    assert response.status_code == status