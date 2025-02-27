"""
Wrapper for boto3 Chime service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_chime/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 Chime client
    chime_client = session.chime.client()
    chime_client: types_boto3_chime.client.ChimeClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_chime.client import ChimeClient
except ImportError:
    ChimeClient = object  # type: ignore[misc,assignment]


class ChimeService(
    ServiceFactory[ChimeClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "chime"
    _SERVICE_PROP = "chime"
