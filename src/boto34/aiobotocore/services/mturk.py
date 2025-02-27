"""
Wrapper for aiobotocore MTurk service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mturk/)

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
    # Returns type annotated aiobotocore MTurk client
    async with session.mturk.create_client() as mturk_client:
        mturk_client: types_aiobotocore_mturk.client.MTurkClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_mturk.client import MTurkClient

from boto34.aiobotocore.service_factory import ServiceFactory


class MTurkService(ServiceFactory[MTurkClient]):
    SERVICE_NAME = "mturk"
    _SERVICE_PROP = "mturk"
