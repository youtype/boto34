"""
Wrapper for boto3 MainframeModernization service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_m2/)

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
    # Returns type annotated boto3 MainframeModernization client
    m2_client = session.m2.client()
    m2_client: types_boto3_m2.client.MainframeModernizationClient
    ```
"""

from __future__ import annotations

from types_boto3_m2.client import MainframeModernizationClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_m2.client import MainframeModernizationClient
except ImportError:
    MainframeModernizationClient = object  # type: ignore[misc,assignment]


class MainframeModernizationService(
    ServiceFactory[MainframeModernizationClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "m2"
    _SERVICE_PROP = "m2"
