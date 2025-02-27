"""
Wrapper for aioboto3 AmplifyUIBuilder service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_amplifyuibuilder/)

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
    # Returns type annotated aioboto3 AmplifyUIBuilder client
    amplifyuibuilder_client = session.amplifyuibuilder.client()
    amplifyuibuilder_client: types_aiobotocore_amplifyuibuilder.client.AmplifyUIBuilderClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_amplifyuibuilder.client import AmplifyUIBuilderClient
except ImportError:
    AmplifyUIBuilderClient = object  # type: ignore[misc,assignment]


class AmplifyUIBuilderService(
    ServiceFactory[AmplifyUIBuilderClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "amplifyuibuilder"
    _SERVICE_PROP = "amplifyuibuilder"
