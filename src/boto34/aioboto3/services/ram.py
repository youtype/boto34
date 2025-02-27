"""
Wrapper for aioboto3 RAM service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_ram/)

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
    # Returns type annotated aioboto3 RAM client
    ram_client = session.ram.client()
    ram_client: types_aiobotocore_ram.client.RAMClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_ram.client import RAMClient

from boto34.aioboto3.service_factory import ServiceFactory


class RAMService(ServiceFactory[RAMClient]):
    SERVICE_NAME = "ram"
    _SERVICE_PROP = "ram"
