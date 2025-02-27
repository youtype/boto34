"""
Wrapper for aioboto3 Greengrass service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_greengrass/)

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
    # Returns type annotated aioboto3 Greengrass client
    greengrass_client = session.greengrass.client()
    greengrass_client: types_aiobotocore_greengrass.client.GreengrassClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_greengrass.client import GreengrassClient
except ImportError:
    GreengrassClient = object  # type: ignore[misc,assignment]


class GreengrassService(
    ServiceFactory[GreengrassClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "greengrass"
    _SERVICE_PROP = "greengrass"
