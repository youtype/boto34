"""
Wrapper for aioboto3 DirectoryService service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_ds/)

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
    # Returns type annotated aioboto3 DirectoryService client
    ds_client = session.ds.client()
    ds_client: types_aiobotocore_ds.client.DirectoryServiceClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_ds.client import DirectoryServiceClient

from boto34.aioboto3.service_factory import ServiceFactory


class DirectoryServiceService(ServiceFactory[DirectoryServiceClient]):
    SERVICE_NAME = "ds"
    _SERVICE_PROP = "ds"
