import requests
import pytest
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

test_user = {
    "name":"inam",
    "email": "inam23@galixo.ai",
    "password": "TestPass123!",
    "otp": "123456",
    "new_password": "NewTestPass456!"
}


def test_register():
    payload = {
        "name":test_user["name"],
        "email": test_user["email"],
        "password": test_user["password"]
    }
    response = requests.post(f"{BASE_URL}/api/vpnuser/register", json=payload)
    assert response.status_code in [200, 201]
    assert "success" in response.json()


def test_login():
    payload = {
        "email": test_user["email"],
        "password": test_user["password"]
    }
    response = requests.post(f"{BASE_URL}/api/vpnuser/login", json=payload)
    assert response.status_code == 200
    assert "token" in response.json()


def test_forgot_password():
    payload = {
        "email": test_user["email"]
    }
    response = requests.post(f"{BASE_URL}/api/vpnuser/forgot-password", json=payload)
    assert response.status_code == 200
    assert "otp_sent" in response.json()


def test_verify_otp():
    payload = {
        "email": test_user["email"],
        "otp": test_user["otp"]
    }
    response = requests.post(f"{BASE_URL}/api/vpnuser/verify-otp", json=payload)
    assert response.status_code == 200
    assert response.json().get("verified") is True


def test_reset_password():
    payload = {
        "email": test_user["email"],
        "otp": test_user["otp"],
        "new_password": test_user["new_password"]
    }
    response = requests.post(f"{BASE_URL}/api/vpnuser/reset-password", json=payload)
    assert response.status_code == 200
    assert "password_reset" in response.json()