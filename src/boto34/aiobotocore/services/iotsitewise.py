"""
Wrapper for aiobotocore IoTSiteWise service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/)

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
    # Returns type annotated aiobotocore IoTSiteWise client
    async with session.iotsitewise.create_client() as iotsitewise_client:
        iotsitewise_client: types_aiobotocore_iotsitewise.client.IoTSiteWiseClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_iotsitewise.client import IoTSiteWiseClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_iotsitewise.client import IoTSiteWiseClient
except ImportError:
    IoTSiteWiseClient = object  # type: ignore[misc,assignment]


class IoTSiteWiseService(
    ServiceFactory[IoTSiteWiseClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "iotsitewise"
    _SERVICE_PROP = "iotsitewise"
