import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture
def client() -> TestClient:
    """Provide a TestClient instance for the FastAPI app."""
    return TestClient(app)


@pytest.fixture
def valid_api_key() -> str:
    """Provide a fake valid API key to use across tests."""
    return "test-secret-key-123"
