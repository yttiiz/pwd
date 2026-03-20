import json
import pytest
from pathlib import Path

from src.config import settings
from src.utils.middleware import get_origins


class TestGetOrigins:
    def test_valid_file_returns_origins(
        self,
        monkeypatch: pytest.MonkeyPatch,
        tmp_path: Path,
    ):
        """Should return the list of origins when the file exists and contains valid content."""
        origins_file = tmp_path / "origins.json"
        origins_file.write_text(
            json.dumps({"origins": ["http://localhost:3000", "https://example.com"]})
        )

        monkeypatch.setattr(settings, "origins_path", str(origins_file))

        result = get_origins()

        assert result == ["http://localhost:3000", "https://example.com"]

    def test_file_without_origins_key_returns_empty_list(
        self,
        monkeypatch: pytest.MonkeyPatch,
        tmp_path: Path,
    ):
        """Should return an empty list when the file exists but does not contain the 'origins' key."""
        origins_file = tmp_path / "origins.json"
        origins_file.write_text(json.dumps({"other_key": "value"}))

        monkeypatch.setattr(settings, "origins_path", str(origins_file))

        result = get_origins()

        assert result == []

    def test_missing_file_returns_empty_list(
        self,
        monkeypatch: pytest.MonkeyPatch,
    ):
        """Should return an empty list when the origins file does not exist."""
        monkeypatch.setattr(settings, "origins_path", "/nonexistent/path/origins.json")

        result = get_origins()

        assert result == []
