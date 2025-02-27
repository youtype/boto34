"""
Wrapper for aiobotocore ACMPCA service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_acm_pca/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore ACMPCA client
    async with session.acm_pca.create_client() as acm_pca_client:
        acm_pca_client: types_aiobotocore_acm_pca.client.ACMPCAClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_acm_pca.client import ACMPCAClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_acm_pca.client import ACMPCAClient
except ImportError:
    ACMPCAClient = object  # type: ignore[misc,assignment]


class ACMPCAService(
    ServiceFactory[ACMPCAClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "acm-pca"
    _SERVICE_PROP = "acm_pca"
