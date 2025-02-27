"""
Wrapper for aiobotocore Greengrass service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_greengrass/)

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
    # Returns type annotated aiobotocore Greengrass client
    async with session.greengrass.create_client() as greengrass_client:
        greengrass_client: types_aiobotocore_greengrass.client.GreengrassClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_greengrass.client import GreengrassClient

from boto34.aiobotocore.service_factory import ServiceFactory


class GreengrassService(ServiceFactory[GreengrassClient]):
    SERVICE_NAME = "greengrass"
    _SERVICE_PROP = "greengrass"
