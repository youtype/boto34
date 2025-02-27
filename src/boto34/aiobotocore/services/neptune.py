"""
Wrapper for aiobotocore Neptune service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune/)

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
    # Returns type annotated aiobotocore Neptune client
    async with session.neptune.create_client() as neptune_client:
        neptune_client: types_aiobotocore_neptune.client.NeptuneClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_neptune.client import NeptuneClient

from boto34.aiobotocore.service_factory import ServiceFactory


class NeptuneService(ServiceFactory[NeptuneClient]):
    SERVICE_NAME = "neptune"
    _SERVICE_PROP = "neptune"
