import requests
import pytest
from websocket import create_connection

BASE_URL = "https://pdevapi.fusionsai.net"


test_user = {
    "email": "testuser@example.com",
    "password": "TestPass123!",
    "otp": "123456",
    "new_password": "NewTestPass456!"
}


def test_register():
    payload = {
        "email": test_user["email"],
        "password": test_user["password"]
    }
    response = requests.post(f"{BASE_URL}/register", json=payload)
    assert response.status_code in [200, 201]
    assert "success" in response.json()


def test_login():
    payload = {
        "email": test_user["email"],
        "password": test_user["password"]
    }
    response = requests.post(f"{BASE_URL}/login", json=payload)
    assert response.status_code == 200
    assert "token" in response.json()


def test_forgot_password():
    payload = {
        "email": test_user["email"]
    }
    response = requests.post(f"{BASE_URL}/forgot-password", json=payload)
    assert response.status_code == 200
    assert "otp_sent" in response.json()


def test_verify_otp():
    payload = {
        "email": test_user["email"],
        "otp": test_user["otp"]
    }
    response = requests.post(f"{BASE_URL}/verify-otp", json=payload)
    assert response.status_code == 200
    assert response.json().get("verified") is True


def test_reset_password():
    payload = {
        "email": test_user["email"],
        "otp": test_user["otp"],
        "new_password": test_user["new_password"]
    }
    response = requests.post(f"{BASE_URL}/reset-password", json=payload)
    assert response.status_code == 200
    assert "password_reset" in response.json()
