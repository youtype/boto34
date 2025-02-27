"""
Wrapper for aioboto3 Braket service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_braket/)

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
    # Returns type annotated aioboto3 Braket client
    braket_client = session.braket.client()
    braket_client: types_aiobotocore_braket.client.BraketClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_braket.client import BraketClient

from boto34.aioboto3.service_factory import ServiceFactory


class BraketService(ServiceFactory[BraketClient]):
    SERVICE_NAME = "braket"
    _SERVICE_PROP = "braket"
