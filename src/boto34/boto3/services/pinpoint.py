"""
Wrapper for boto3 Pinpoint service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_pinpoint/)

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
    # Returns type annotated boto3 Pinpoint client
    pinpoint_client = session.pinpoint.client()
    pinpoint_client: types_boto3_pinpoint.client.PinpointClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_pinpoint.client import PinpointClient
except ImportError:
    PinpointClient = object  # type: ignore[misc,assignment]


class PinpointService(
    ServiceFactory[PinpointClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "pinpoint"
    _SERVICE_PROP = "pinpoint"
