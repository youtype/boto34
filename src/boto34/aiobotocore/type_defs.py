"""
Type definitions.

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from typing import TypedDict

from aiobotocore.config import AioConfig


class ClientKwargs(TypedDict, total=False):
    """
    Keyword arguments for aiobotocore.create_client.
    """

    region_name: str | None
    api_version: str | None
    use_ssl: bool | None
    verify: bool | str | None
    endpoint_url: str | None
    aws_access_key_id: str | None
    aws_secret_access_key: str | None
    aws_session_token: str | None
    config: AioConfig | None
