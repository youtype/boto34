"""
Wrapper for aioboto3 Ivschat service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_ivschat/)

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
    # Returns type annotated aioboto3 Ivschat client
    ivschat_client = session.ivschat.client()
    ivschat_client: types_aiobotocore_ivschat.client.IvschatClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_ivschat.client import IvschatClient

from boto34.aioboto3.service_factory import ServiceFactory


class IvschatService(ServiceFactory[IvschatClient]):
    SERVICE_NAME = "ivschat"
    _SERVICE_PROP = "ivschat"
