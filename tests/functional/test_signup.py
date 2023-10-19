from tests.mocks import signup


def test_create_a_new_user(test_client):
    status = 201
    response = test_client.post("/sign-up/", headers={"Content-Type": "application/json"}, json=signup.payload)
    assert response.status_code == status


def test_tries_to_create_a_user_with_an_already_existing_username(test_client):
    status = 422
    response = test_client.post("/sign-up/", headers={"Content-Type": "application/json"}, json=signup.payload)
    assert response.status_code == status


def test_tries_to_create_a_user_with_less_than_10_characters_in_the_password(test_client):
    status = 420
    response = test_client.post("/sign-up/", headers={"Content-Type": "application/json"}, json=signup.payload_invalid)
    assert response.status_code == status