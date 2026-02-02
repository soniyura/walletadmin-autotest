import os
import pytest
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL")

@pytest.fixture(scope="session")
def creds():
    return {
        "username": os.getenv("ADMIN_USER"),
        "password": os.getenv("ADMIN_PASS"),
    }
