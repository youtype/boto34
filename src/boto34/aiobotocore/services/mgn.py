"""
Wrapper for aiobotocore Mgn service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mgn/)

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
    # Returns type annotated aiobotocore Mgn client
    async with session.mgn.create_client() as mgn_client:
        mgn_client: types_aiobotocore_mgn.client.MgnClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_mgn.client import MgnClient

from boto34.aiobotocore.service_factory import ServiceFactory


class MgnService(ServiceFactory[MgnClient]):
    SERVICE_NAME = "mgn"
    _SERVICE_PROP = "mgn"
