"""
Wrapper for boto3 IoTSecureTunneling service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_iotsecuretunneling/)

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
    # Returns type annotated boto3 IoTSecureTunneling client
    iotsecuretunneling_client = session.iotsecuretunneling.client()
    iotsecuretunneling_client: types_boto3_iotsecuretunneling.client.IoTSecureTunnelingClient
    ```
"""

from __future__ import annotations

from types_boto3_iotsecuretunneling.client import IoTSecureTunnelingClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_iotsecuretunneling.client import IoTSecureTunnelingClient
except ImportError:
    IoTSecureTunnelingClient = object  # type: ignore[misc,assignment]


class IoTSecureTunnelingService(
    ServiceFactory[IoTSecureTunnelingClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "iotsecuretunneling"
    _SERVICE_PROP = "iotsecuretunneling"
