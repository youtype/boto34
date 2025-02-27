"""
Wrapper for aiobotocore FreeTier service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_freetier/)

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
    # Returns type annotated aiobotocore FreeTier client
    async with session.freetier.create_client() as freetier_client:
        freetier_client: types_aiobotocore_freetier.client.FreeTierClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_freetier.client import FreeTierClient
except ImportError:
    FreeTierClient = object  # type: ignore[misc,assignment]


class FreeTierService(
    ServiceFactory[FreeTierClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "freetier"
    _SERVICE_PROP = "freetier"
