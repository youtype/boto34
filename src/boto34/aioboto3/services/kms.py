"""
Wrapper for aioboto3 KMS service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_kms/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 KMS client
    kms_client = session.kms.client()
    kms_client: types_aiobotocore_kms.client.KMSClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_kms.client import KMSClient
except ImportError:
    KMSClient = object  # type: ignore[misc,assignment]


class KMSService(
    ServiceFactory[KMSClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "kms"
    _SERVICE_PROP = "kms"
