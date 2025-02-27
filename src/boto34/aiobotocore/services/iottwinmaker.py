"""
Wrapper for aiobotocore IoTTwinMaker service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/)

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
    # Returns type annotated aiobotocore IoTTwinMaker client
    async with session.iottwinmaker.create_client() as iottwinmaker_client:
        iottwinmaker_client: types_aiobotocore_iottwinmaker.client.IoTTwinMakerClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_iottwinmaker.client import IoTTwinMakerClient

from boto34.aiobotocore.service_factory import ServiceFactory


class IoTTwinMakerService(ServiceFactory[IoTTwinMakerClient]):
    SERVICE_NAME = "iottwinmaker"
    _SERVICE_PROP = "iottwinmaker"
