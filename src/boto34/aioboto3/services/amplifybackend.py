"""
Wrapper for aioboto3 AmplifyBackend service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_amplifybackend/)

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
    # Returns type annotated aioboto3 AmplifyBackend client
    amplifybackend_client = session.amplifybackend.client()
    amplifybackend_client: types_aiobotocore_amplifybackend.client.AmplifyBackendClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_amplifybackend.client import AmplifyBackendClient
except ImportError:
    AmplifyBackendClient = object  # type: ignore[misc,assignment]


class AmplifyBackendService(
    ServiceFactory[AmplifyBackendClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "amplifybackend"
    _SERVICE_PROP = "amplifybackend"
