"""
Wrapper for boto3 Keyspaces service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_keyspaces/)

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
    # Returns type annotated boto3 Keyspaces client
    keyspaces_client = session.keyspaces.client()
    keyspaces_client: types_boto3_keyspaces.client.KeyspacesClient
    ```
"""

from __future__ import annotations

from types_boto3_keyspaces.client import KeyspacesClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_keyspaces.client import KeyspacesClient
except ImportError:
    KeyspacesClient = object  # type: ignore[misc,assignment]


class KeyspacesService(
    ServiceFactory[KeyspacesClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "keyspaces"
    _SERVICE_PROP = "keyspaces"
