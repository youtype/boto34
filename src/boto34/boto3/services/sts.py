"""
Wrapper for boto3 STS service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sts/)

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
    # Returns type annotated boto3 STS client
    sts_client = session.sts.client()
    sts_client: types_boto3_sts.client.STSClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_sts.client import STSClient
except ImportError:
    STSClient = object  # type: ignore[misc,assignment]


class STSService(
    ServiceFactory[STSClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "sts"
    _SERVICE_PROP = "sts"
