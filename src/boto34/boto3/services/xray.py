"""
Wrapper for boto3 XRay service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_xray/)

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
    # Returns type annotated boto3 XRay client
    xray_client = session.xray.client()
    xray_client: types_boto3_xray.client.XRayClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_xray.client import XRayClient
except ImportError:
    XRayClient = object  # type: ignore[misc,assignment]


class XRayService(
    ServiceFactory[XRayClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "xray"
    _SERVICE_PROP = "xray"
