"""
Wrapper for boto3 ACM service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_acm/)

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
    # Returns type annotated boto3 ACM client
    acm_client = session.acm.client()
    acm_client: types_boto3_acm.client.ACMClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_acm.client import ACMClient
except ImportError:
    ACMClient = object  # type: ignore[misc,assignment]


class ACMService(
    ServiceFactory[ACMClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "acm"
    _SERVICE_PROP = "acm"
