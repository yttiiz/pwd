import pytest
from fastapi.testclient import TestClient
from pathlib import Path

from src.config import settings


class TestDatabaseRoute:
    def test_no_api_key_returns_403(self, client: TestClient):
        """Should return 403 when no api_key query param is provided."""
        response = client.get("/database/")

        assert response.status_code == 403
        assert response.json()["detail"] == "You have to provide an api key"

    def test_wrong_api_key_returns_403(
        self,
        client: TestClient,
        valid_api_key: str,
        monkeypatch: pytest.MonkeyPatch,
    ):
        """Should return 403 when the provided api_key does not match."""
        monkeypatch.setattr(settings, "api_key", valid_api_key)

        response = client.get("/database/", params={"api_key": "wrong-key"})

        assert response.status_code == 403
        assert (
            response.json()["detail"] == "You are not authorized to get the resource."
        )

    def test_valid_api_key_but_missing_file_returns_404(
        self,
        client: TestClient,
        valid_api_key: str,
        monkeypatch: pytest.MonkeyPatch,
    ):
        """Should return 404 when the api_key is valid but the database file does not exist."""
        monkeypatch.setattr(settings, "api_key", valid_api_key)
        monkeypatch.setattr(
            settings, "pwd_database_path", "/nonexistent/path/database.kdbx"
        )

        response = client.get("/database/", params={"api_key": valid_api_key})

        assert response.status_code == 404
        assert response.json()["detail"] == "Database file not found"

    def test_valid_api_key_and_existing_file_returns_200(
        self,
        client: TestClient,
        valid_api_key: str,
        monkeypatch: pytest.MonkeyPatch,
        tmp_path: Path,
    ):
        """Should return 200 with the file when the api_key is valid and the database file exists."""
        db_file = tmp_path / "database.kdbx"
        _ = db_file.write_bytes(b"fake database content")

        monkeypatch.setattr(settings, "api_key", valid_api_key)
        monkeypatch.setattr(settings, "pwd_database_path", str(db_file))

        response = client.get("/database/", params={"api_key": valid_api_key})

        assert response.status_code == 200
        assert response.headers["content-type"] == "application/octet-stream"
        assert "database.kdbx" in response.headers["content-disposition"]
        assert response.content == b"fake database content"
