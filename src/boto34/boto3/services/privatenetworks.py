"""
Wrapper for boto3 Private5G service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_privatenetworks/)

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
    # Returns type annotated boto3 Private5G client
    privatenetworks_client = session.privatenetworks.client()
    privatenetworks_client: types_boto3_privatenetworks.client.Private5GClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_privatenetworks.client import Private5GClient
except ImportError:
    Private5GClient = object  # type: ignore[misc,assignment]


class Private5GService(
    ServiceFactory[Private5GClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "privatenetworks"
    _SERVICE_PROP = "privatenetworks"
