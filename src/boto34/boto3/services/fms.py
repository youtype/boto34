"""
Wrapper for boto3 FMS service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_fms/)

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
    # Returns type annotated boto3 FMS client
    fms_client = session.fms.client()
    fms_client: types_boto3_fms.client.FMSClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_fms.client import FMSClient
except ImportError:
    FMSClient = object  # type: ignore[misc,assignment]


class FMSService(
    ServiceFactory[FMSClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "fms"
    _SERVICE_PROP = "fms"
