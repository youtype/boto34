"""
Wrapper for boto3 Kendra service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kendra/)

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
    # Returns type annotated boto3 Kendra client
    kendra_client = session.kendra.client()
    kendra_client: types_boto3_kendra.client.KendraClient
    ```
"""

from __future__ import annotations

from types_boto3_kendra.client import KendraClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_kendra.client import KendraClient
except ImportError:
    KendraClient = object  # type: ignore[misc,assignment]


class KendraService(
    ServiceFactory[KendraClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "kendra"
    _SERVICE_PROP = "kendra"
