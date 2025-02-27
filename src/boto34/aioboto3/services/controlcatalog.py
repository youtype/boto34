"""
Wrapper for aioboto3 ControlCatalog service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_controlcatalog/)

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
    # Returns type annotated aioboto3 ControlCatalog client
    controlcatalog_client = session.controlcatalog.client()
    controlcatalog_client: types_aiobotocore_controlcatalog.client.ControlCatalogClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_controlcatalog.client import ControlCatalogClient

from boto34.aioboto3.service_factory import ServiceFactory


class ControlCatalogService(ServiceFactory[ControlCatalogClient]):
    SERVICE_NAME = "controlcatalog"
    _SERVICE_PROP = "controlcatalog"
