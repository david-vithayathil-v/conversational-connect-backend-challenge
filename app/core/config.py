from __future__ import annotations

import os
from functools import lru_cache
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


def _existing_env_files() -> tuple[str, ...] | None:
    env_file_override = os.environ.get("APP_ENV_FILE")
    environment = os.environ.get("APP_ENVIRONMENT")

    candidates: list[Path] = []
    if env_file_override:
        candidates.append(Path(env_file_override))

    # Preferred naming: env/<environment>.env
    if environment:
        candidates.extend(
            [
                Path(f"env/{environment}.env"),
            ]
        )

    # Base env file (local dev convenience)
    candidates.append(Path("env/dev.env"))

    # Backward compatible fallbacks (older naming)
    candidates.extend(
        [
            Path("env/.env"),
            Path("env/.env.local"),
        ]
    )
    candidates.append(Path(".env"))

    existing = [str(path) for path in candidates if path.exists()]
    return tuple(existing) if existing else None


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=_existing_env_files(),
        env_prefix="APP_",
        case_sensitive=False,
        extra="ignore",
    )

    service_name: str = Field(default="conversational-connect")
    environment: str = Field(default="local")

    api_v1_prefix: str = Field(default="/api/v1")

    log_level: str = Field(default="INFO")
    log_format: str = Field(default="json")


@lru_cache
def get_settings() -> Settings:
    return Settings()
