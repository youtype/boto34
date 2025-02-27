"""
Wrapper for aioboto3 EndUserMessagingSocial service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_socialmessaging/)

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
    # Returns type annotated aioboto3 EndUserMessagingSocial client
    socialmessaging_client = session.socialmessaging.client()
    socialmessaging_client: types_aiobotocore_socialmessaging.client.EndUserMessagingSocialClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_socialmessaging.client import EndUserMessagingSocialClient

from boto34.aioboto3.service_factory import ServiceFactory


class EndUserMessagingSocialService(ServiceFactory[EndUserMessagingSocialClient]):
    SERVICE_NAME = "socialmessaging"
    _SERVICE_PROP = "socialmessaging"
