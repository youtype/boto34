"""
Wrapper for aiobotocore EFS service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_efs/)

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
    # Returns type annotated aiobotocore EFS client
    async with session.efs.create_client() as efs_client:
        efs_client: types_aiobotocore_efs.client.EFSClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_efs.client import EFSClient

from boto34.aiobotocore.service_factory import ServiceFactory


class EFSService(ServiceFactory[EFSClient]):
    SERVICE_NAME = "efs"
    _SERVICE_PROP = "efs"
