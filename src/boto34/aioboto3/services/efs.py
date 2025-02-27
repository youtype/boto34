"""
Wrapper for aioboto3 EFS service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_efs/)

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
    # Returns type annotated aioboto3 EFS client
    efs_client = session.efs.client()
    efs_client: types_aiobotocore_efs.client.EFSClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_efs.client import EFSClient

from boto34.aioboto3.service_factory import ServiceFactory


class EFSService(ServiceFactory[EFSClient]):
    SERVICE_NAME = "efs"
    _SERVICE_PROP = "efs"
