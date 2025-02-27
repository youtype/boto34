"""
Wrapper for aiobotocore ConnectCases service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectcases/)

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
    # Returns type annotated aiobotocore ConnectCases client
    async with session.connectcases.create_client() as connectcases_client:
        connectcases_client: types_aiobotocore_connectcases.client.ConnectCasesClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_connectcases.client import ConnectCasesClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ConnectCasesService(ServiceFactory[ConnectCasesClient]):
    SERVICE_NAME = "connectcases"
    _SERVICE_PROP = "connectcases"
