"""
Wrapper for aiobotocore DeadlineCloud service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_deadline/)

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
    # Returns type annotated aiobotocore DeadlineCloud client
    async with session.deadline.create_client() as deadline_client:
        deadline_client: types_aiobotocore_deadline.client.DeadlineCloudClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_deadline.client import DeadlineCloudClient

from boto34.aiobotocore.service_factory import ServiceFactory


class DeadlineCloudService(ServiceFactory[DeadlineCloudClient]):
    SERVICE_NAME = "deadline"
    _SERVICE_PROP = "deadline"
