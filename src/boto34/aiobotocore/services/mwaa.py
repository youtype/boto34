"""
Wrapper for aiobotocore MWAA service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mwaa/)

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
    # Returns type annotated aiobotocore MWAA client
    async with session.mwaa.create_client() as mwaa_client:
        mwaa_client: types_aiobotocore_mwaa.client.MWAAClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_mwaa.client import MWAAClient
except ImportError:
    MWAAClient = object  # type: ignore[misc,assignment]


class MWAAService(
    ServiceFactory[MWAAClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "mwaa"
    _SERVICE_PROP = "mwaa"
