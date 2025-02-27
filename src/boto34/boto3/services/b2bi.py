"""
Wrapper for boto3 B2BI service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_b2bi/)

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
    # Returns type annotated boto3 B2BI client
    b2bi_client = session.b2bi.client()
    b2bi_client: types_boto3_b2bi.client.B2BIClient
    ```
"""

from __future__ import annotations

from types_boto3_b2bi.client import B2BIClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_b2bi.client import B2BIClient
except ImportError:
    B2BIClient = object  # type: ignore[misc,assignment]


class B2BIService(
    ServiceFactory[B2BIClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "b2bi"
    _SERVICE_PROP = "b2bi"
