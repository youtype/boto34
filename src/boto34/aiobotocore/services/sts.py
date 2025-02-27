"""
Wrapper for aiobotocore STS service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sts/)

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
    # Returns type annotated aiobotocore STS client
    async with session.sts.create_client() as sts_client:
        sts_client: types_aiobotocore_sts.client.STSClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_sts.client import STSClient

from boto34.aiobotocore.service_factory import ServiceFactory


class STSService(ServiceFactory[STSClient]):
    SERVICE_NAME = "sts"
    _SERVICE_PROP = "sts"
