"""
Wrapper for boto3 TelcoNetworkBuilder service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_tnb/)

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
    # Returns type annotated boto3 TelcoNetworkBuilder client
    tnb_client = session.tnb.client()
    tnb_client: types_boto3_tnb.client.TelcoNetworkBuilderClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_tnb.client import TelcoNetworkBuilderClient
except ImportError:
    TelcoNetworkBuilderClient = object  # type: ignore[misc,assignment]


class TelcoNetworkBuilderService(
    ServiceFactory[TelcoNetworkBuilderClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "tnb"
    _SERVICE_PROP = "tnb"
