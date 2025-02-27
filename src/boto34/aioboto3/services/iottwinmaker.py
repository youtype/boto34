"""
Wrapper for aioboto3 IoTTwinMaker service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_iottwinmaker/)

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
    # Returns type annotated aioboto3 IoTTwinMaker client
    iottwinmaker_client = session.iottwinmaker.client()
    iottwinmaker_client: types_aiobotocore_iottwinmaker.client.IoTTwinMakerClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_iottwinmaker.client import IoTTwinMakerClient

from boto34.aioboto3.service_factory import ServiceFactory


class IoTTwinMakerService(ServiceFactory[IoTTwinMakerClient]):
    SERVICE_NAME = "iottwinmaker"
    _SERVICE_PROP = "iottwinmaker"
