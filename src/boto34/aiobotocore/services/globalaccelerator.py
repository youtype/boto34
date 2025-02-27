"""
Wrapper for aiobotocore GlobalAccelerator service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_globalaccelerator/)

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
    # Returns type annotated aiobotocore GlobalAccelerator client
    async with session.globalaccelerator.create_client() as globalaccelerator_client:
        globalaccelerator_client: types_aiobotocore_globalaccelerator.client.GlobalAcceleratorClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_globalaccelerator.client import GlobalAcceleratorClient

from boto34.aiobotocore.service_factory import ServiceFactory


class GlobalAcceleratorService(ServiceFactory[GlobalAcceleratorClient]):
    SERVICE_NAME = "globalaccelerator"
    _SERVICE_PROP = "globalaccelerator"
