"""
Wrapper for boto3 KMS service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kms/)

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
    # Returns type annotated boto3 KMS client
    kms_client = session.kms.client()
    kms_client: types_boto3_kms.client.KMSClient
    ```
"""

from __future__ import annotations

from types_boto3_kms.client import KMSClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_kms.client import KMSClient
except ImportError:
    KMSClient = object  # type: ignore[misc,assignment]


class KMSService(
    ServiceFactory[KMSClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "kms"
    _SERVICE_PROP = "kms"
