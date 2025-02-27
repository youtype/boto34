"""
Wrapper for aioboto3 IoTSiteWise service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_iotsitewise/)

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
    # Returns type annotated aioboto3 IoTSiteWise client
    iotsitewise_client = session.iotsitewise.client()
    iotsitewise_client: types_aiobotocore_iotsitewise.client.IoTSiteWiseClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_iotsitewise.client import IoTSiteWiseClient

from boto34.aioboto3.service_factory import ServiceFactory


class IoTSiteWiseService(ServiceFactory[IoTSiteWiseClient]):
    SERVICE_NAME = "iotsitewise"
    _SERVICE_PROP = "iotsitewise"
