"""
Wrapper for aiobotocore Athena service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/)

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
    # Returns type annotated aiobotocore Athena client
    async with session.athena.create_client() as athena_client:
        athena_client: types_aiobotocore_athena.client.AthenaClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_athena.client import AthenaClient
except ImportError:
    AthenaClient = object  # type: ignore[misc,assignment]


class AthenaService(
    ServiceFactory[AthenaClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "athena"
    _SERVICE_PROP = "athena"
