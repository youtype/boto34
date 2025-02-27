"""
Wrapper for aiobotocore Inspector2 service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector2/)

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
    # Returns type annotated aiobotocore Inspector2 client
    async with session.inspector2.create_client() as inspector2_client:
        inspector2_client: types_aiobotocore_inspector2.client.Inspector2Client
    ```
"""

from __future__ import annotations

from types_aiobotocore_inspector2.client import Inspector2Client

from boto34.aiobotocore.service_factory import ServiceFactory


class Inspector2Service(ServiceFactory[Inspector2Client]):
    SERVICE_NAME = "inspector2"
    _SERVICE_PROP = "inspector2"
