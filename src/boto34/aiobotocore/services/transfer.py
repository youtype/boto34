"""
Wrapper for aiobotocore Transfer service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transfer/)

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
    # Returns type annotated aiobotocore Transfer client
    async with session.transfer.create_client() as transfer_client:
        transfer_client: types_aiobotocore_transfer.client.TransferClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_transfer.client import TransferClient

from boto34.aiobotocore.service_factory import ServiceFactory


class TransferService(ServiceFactory[TransferClient]):
    SERVICE_NAME = "transfer"
    _SERVICE_PROP = "transfer"
