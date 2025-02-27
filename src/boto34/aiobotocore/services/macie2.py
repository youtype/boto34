"""
Wrapper for aiobotocore Macie2 service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_macie2/)

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
    # Returns type annotated aiobotocore Macie2 client
    async with session.macie2.create_client() as macie2_client:
        macie2_client: types_aiobotocore_macie2.client.Macie2Client
    ```
"""

from __future__ import annotations

from types_aiobotocore_macie2.client import Macie2Client

from boto34.aiobotocore.service_factory import ServiceFactory


class Macie2Service(ServiceFactory[Macie2Client]):
    SERVICE_NAME = "macie2"
    _SERVICE_PROP = "macie2"
