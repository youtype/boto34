"""
Wrapper for boto3 PI service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_pi/)

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
    # Returns type annotated boto3 PI client
    pi_client = session.pi.client()
    pi_client: types_boto3_pi.client.PIClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_pi.client import PIClient
except ImportError:
    PIClient = object  # type: ignore[misc,assignment]


class PIService(
    ServiceFactory[PIClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "pi"
    _SERVICE_PROP = "pi"
