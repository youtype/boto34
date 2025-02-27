"""
Wrapper for aioboto3 EMRServerless service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_emr_serverless/)

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
    # Returns type annotated aioboto3 EMRServerless client
    emr_serverless_client = session.emr_serverless.client()
    emr_serverless_client: types_aiobotocore_emr_serverless.client.EMRServerlessClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_emr_serverless.client import EMRServerlessClient
except ImportError:
    EMRServerlessClient = object  # type: ignore[misc,assignment]


class EMRServerlessService(
    ServiceFactory[EMRServerlessClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "emr-serverless"
    _SERVICE_PROP = "emr_serverless"
