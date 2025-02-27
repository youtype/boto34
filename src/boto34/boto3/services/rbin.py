"""
Wrapper for boto3 RecycleBin service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_rbin/)

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
    # Returns type annotated boto3 RecycleBin client
    rbin_client = session.rbin.client()
    rbin_client: types_boto3_rbin.client.RecycleBinClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_rbin.client import RecycleBinClient
except ImportError:
    RecycleBinClient = object  # type: ignore[misc,assignment]


class RecycleBinService(
    ServiceFactory[RecycleBinClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "rbin"
    _SERVICE_PROP = "rbin"
