"""
Wrapper for aioboto3 LookoutforVision service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_lookoutvision/)

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
    # Returns type annotated aioboto3 LookoutforVision client
    lookoutvision_client = session.lookoutvision.client()
    lookoutvision_client: types_aiobotocore_lookoutvision.client.LookoutforVisionClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_lookoutvision.client import LookoutforVisionClient

from boto34.aioboto3.service_factory import ServiceFactory


class LookoutforVisionService(ServiceFactory[LookoutforVisionClient]):
    SERVICE_NAME = "lookoutvision"
    _SERVICE_PROP = "lookoutvision"
