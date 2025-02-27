"""
Wrapper for aioboto3 Snowball service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_snowball/)

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
    # Returns type annotated aioboto3 Snowball client
    snowball_client = session.snowball.client()
    snowball_client: types_aiobotocore_snowball.client.SnowballClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_snowball.client import SnowballClient

from boto34.aioboto3.service_factory import ServiceFactory


class SnowballService(ServiceFactory[SnowballClient]):
    SERVICE_NAME = "snowball"
    _SERVICE_PROP = "snowball"
