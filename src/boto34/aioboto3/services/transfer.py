"""
Wrapper for aioboto3 Transfer service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_transfer/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 Transfer client
    transfer_client = session.transfer.client()
    transfer_client: types_aiobotocore_transfer.client.TransferClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_transfer.client import TransferClient

from boto34.aioboto3.service_factory import ServiceFactory


class TransferService(ServiceFactory[TransferClient]):
    SERVICE_NAME = "transfer"
    _SERVICE_PROP = "transfer"
