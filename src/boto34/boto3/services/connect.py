"""
Wrapper for boto3 Connect service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_connect/)

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
    # Returns type annotated boto3 Connect client
    connect_client = session.connect.client()
    connect_client: types_boto3_connect.client.ConnectClient
    ```
"""

from __future__ import annotations

from types_boto3_connect.client import ConnectClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_connect.client import ConnectClient
except ImportError:
    ConnectClient = object  # type: ignore[misc,assignment]


class ConnectService(
    ServiceFactory[ConnectClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "connect"
    _SERVICE_PROP = "connect"
