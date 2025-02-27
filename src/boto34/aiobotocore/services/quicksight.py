"""
Wrapper for aiobotocore QuickSight service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_quicksight/)

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
    # Returns type annotated aiobotocore QuickSight client
    async with session.quicksight.create_client() as quicksight_client:
        quicksight_client: types_aiobotocore_quicksight.client.QuickSightClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_quicksight.client import QuickSightClient

from boto34.aiobotocore.service_factory import ServiceFactory


class QuickSightService(ServiceFactory[QuickSightClient]):
    SERVICE_NAME = "quicksight"
    _SERVICE_PROP = "quicksight"
