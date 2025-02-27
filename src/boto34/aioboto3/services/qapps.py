"""
Wrapper for aioboto3 QApps service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_qapps/)

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
    # Returns type annotated aioboto3 QApps client
    qapps_client = session.qapps.client()
    qapps_client: types_aiobotocore_qapps.client.QAppsClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_qapps.client import QAppsClient

from boto34.aioboto3.service_factory import ServiceFactory


class QAppsService(ServiceFactory[QAppsClient]):
    SERVICE_NAME = "qapps"
    _SERVICE_PROP = "qapps"
