"""
Wrapper for aioboto3 CloudWatchRUM service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_rum/)

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
    # Returns type annotated aioboto3 CloudWatchRUM client
    rum_client = session.rum.client()
    rum_client: types_aiobotocore_rum.client.CloudWatchRUMClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_rum.client import CloudWatchRUMClient

from boto34.aioboto3.service_factory import ServiceFactory


class CloudWatchRUMService(ServiceFactory[CloudWatchRUMClient]):
    SERVICE_NAME = "rum"
    _SERVICE_PROP = "rum"
