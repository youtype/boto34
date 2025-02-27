"""
Wrapper for aioboto3 Lightsail service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_lightsail/)

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
    # Returns type annotated aioboto3 Lightsail client
    lightsail_client = session.lightsail.client()
    lightsail_client: types_aiobotocore_lightsail.client.LightsailClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_lightsail.client import LightsailClient

from boto34.aioboto3.service_factory import ServiceFactory


class LightsailService(ServiceFactory[LightsailClient]):
    SERVICE_NAME = "lightsail"
    _SERVICE_PROP = "lightsail"
