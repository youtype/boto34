"""
Wrapper for aioboto3 STS service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_sts/)

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
    # Returns type annotated aioboto3 STS client
    sts_client = session.sts.client()
    sts_client: types_aiobotocore_sts.client.STSClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_sts.client import STSClient

from boto34.aioboto3.service_factory import ServiceFactory


class STSService(ServiceFactory[STSClient]):
    SERVICE_NAME = "sts"
    _SERVICE_PROP = "sts"
