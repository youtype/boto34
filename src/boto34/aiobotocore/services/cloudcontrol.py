"""
Wrapper for aiobotocore CloudControlApi service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudcontrol/)

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
    # Returns type annotated aiobotocore CloudControlApi client
    async with session.cloudcontrol.create_client() as cloudcontrol_client:
        cloudcontrol_client: types_aiobotocore_cloudcontrol.client.CloudControlApiClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_cloudcontrol.client import CloudControlApiClient

from boto34.aiobotocore.service_factory import ServiceFactory


class CloudControlApiService(ServiceFactory[CloudControlApiClient]):
    SERVICE_NAME = "cloudcontrol"
    _SERVICE_PROP = "cloudcontrol"
