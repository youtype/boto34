"""
Wrapper for boto3 ACMPCA service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_acm_pca/)

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
    # Returns type annotated boto3 ACMPCA client
    acm_pca_client = session.acm_pca.client()
    acm_pca_client: types_boto3_acm_pca.client.ACMPCAClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_acm_pca.client import ACMPCAClient
except ImportError:
    ACMPCAClient = object  # type: ignore[misc,assignment]


class ACMPCAService(
    ServiceFactory[ACMPCAClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "acm-pca"
    _SERVICE_PROP = "acm_pca"
