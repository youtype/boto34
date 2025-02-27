"""
Wrapper for aioboto3 EMR service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_emr/)

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
    # Returns type annotated aioboto3 EMR client
    emr_client = session.emr.client()
    emr_client: types_aiobotocore_emr.client.EMRClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_emr.client import EMRClient
except ImportError:
    EMRClient = object  # type: ignore[misc,assignment]


class EMRService(
    ServiceFactory[EMRClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "emr"
    _SERVICE_PROP = "emr"
