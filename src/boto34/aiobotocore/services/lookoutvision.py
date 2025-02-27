"""
Wrapper for aiobotocore LookoutforVision service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutvision/)

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
    # Returns type annotated aiobotocore LookoutforVision client
    async with session.lookoutvision.create_client() as lookoutvision_client:
        lookoutvision_client: types_aiobotocore_lookoutvision.client.LookoutforVisionClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_lookoutvision.client import LookoutforVisionClient
except ImportError:
    LookoutforVisionClient = object  # type: ignore[misc,assignment]


class LookoutforVisionService(
    ServiceFactory[LookoutforVisionClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "lookoutvision"
    _SERVICE_PROP = "lookoutvision"
