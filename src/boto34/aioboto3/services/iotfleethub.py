"""
Wrapper for aioboto3 IoTFleetHub service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_iotfleethub/)

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
    # Returns type annotated aioboto3 IoTFleetHub client
    iotfleethub_client = session.iotfleethub.client()
    iotfleethub_client: types_aiobotocore_iotfleethub.client.IoTFleetHubClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_iotfleethub.client import IoTFleetHubClient

from boto34.aioboto3.service_factory import ServiceFactory


class IoTFleetHubService(ServiceFactory[IoTFleetHubClient]):
    SERVICE_NAME = "iotfleethub"
    _SERVICE_PROP = "iotfleethub"
