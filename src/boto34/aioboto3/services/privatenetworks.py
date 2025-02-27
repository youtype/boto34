"""
Wrapper for aioboto3 Private5G service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_privatenetworks/)

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
    # Returns type annotated aioboto3 Private5G client
    privatenetworks_client = session.privatenetworks.client()
    privatenetworks_client: types_aiobotocore_privatenetworks.client.Private5GClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_privatenetworks.client import Private5GClient

from boto34.aioboto3.service_factory import ServiceFactory


class Private5GService(ServiceFactory[Private5GClient]):
    SERVICE_NAME = "privatenetworks"
    _SERVICE_PROP = "privatenetworks"
