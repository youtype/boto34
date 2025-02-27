"""
Wrapper for aiobotocore DAX service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dax/)

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
    # Returns type annotated aiobotocore DAX client
    async with session.dax.create_client() as dax_client:
        dax_client: types_aiobotocore_dax.client.DAXClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_dax.client import DAXClient
except ImportError:
    DAXClient = object  # type: ignore[misc,assignment]


class DAXService(
    ServiceFactory[DAXClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "dax"
    _SERVICE_PROP = "dax"
