"""
Type definitions.

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    from botocore.config import Config


class ClientKwargs(TypedDict, total=False):
    """
    Keyword arguments for boto3.client.
    """

    region_name: str | None
    api_version: str | None
    use_ssl: bool | None
    verify: bool | str | None
    endpoint_url: str | None
    aws_access_key_id: str | None
    aws_secret_access_key: str | None
    aws_session_token: str | None
    config: Config | None


class ResourceKwargs(TypedDict, total=False):
    """
    Keyword arguments for boto3.resource.
    """

    region_name: str | None
    api_version: str | None
    use_ssl: bool | None
    verify: bool | str | None
    endpoint_url: str | None
    aws_access_key_id: str | None
    aws_secret_access_key: str | None
    aws_session_token: str | None
    config: Config | None
