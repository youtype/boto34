"""
Wrapper for aioboto3 CloudDirectory service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_clouddirectory/)

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
    # Returns type annotated aioboto3 CloudDirectory client
    clouddirectory_client = session.clouddirectory.client()
    clouddirectory_client: types_aiobotocore_clouddirectory.client.CloudDirectoryClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_clouddirectory.client import CloudDirectoryClient

from boto34.aioboto3.service_factory import ServiceFactory


class CloudDirectoryService(ServiceFactory[CloudDirectoryClient]):
    SERVICE_NAME = "clouddirectory"
    _SERVICE_PROP = "clouddirectory"
