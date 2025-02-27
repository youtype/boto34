"""
Wrapper for aiobotocore Drs service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_drs/)

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
    # Returns type annotated aiobotocore Drs client
    async with session.drs.create_client() as drs_client:
        drs_client: types_aiobotocore_drs.client.DrsClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_drs.client import DrsClient
except ImportError:
    DrsClient = object  # type: ignore[misc,assignment]


class DrsService(
    ServiceFactory[DrsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "drs"
    _SERVICE_PROP = "drs"
