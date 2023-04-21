import httpx
import pytest


@pytest.mark.asyncio
async def test_sign_new_user(default_client: httpx.AsyncClient) -> None:
    """
        The function tests the sign-up endpoint.
    """

    # request data
    payload = {
        "email": "testuser@packt.com",
        "password": "testpassword",
    }

    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }

    # expected response
    test_response = {
        "message": "User created successfully"
    }

    # initiate the request
    response = await default_client.post("/user/signup", json=payload, headers=headers)

    # compare the responses to be sure whether the request was successful
    assert response.status_code == 200
    assert response.json() == test_response
