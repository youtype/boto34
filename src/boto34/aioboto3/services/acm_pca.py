"""
Wrapper for aioboto3 ACMPCA service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_acm_pca/)

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
    # Returns type annotated aioboto3 ACMPCA client
    acm_pca_client = session.acm_pca.client()
    acm_pca_client: types_aiobotocore_acm_pca.client.ACMPCAClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_acm_pca.client import ACMPCAClient
except ImportError:
    ACMPCAClient = object  # type: ignore[misc,assignment]


class ACMPCAService(
    ServiceFactory[ACMPCAClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "acm-pca"
    _SERVICE_PROP = "acm_pca"
