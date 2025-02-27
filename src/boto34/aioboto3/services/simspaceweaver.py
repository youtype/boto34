"""
Wrapper for aioboto3 SimSpaceWeaver service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_simspaceweaver/)

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
    # Returns type annotated aioboto3 SimSpaceWeaver client
    simspaceweaver_client = session.simspaceweaver.client()
    simspaceweaver_client: types_aiobotocore_simspaceweaver.client.SimSpaceWeaverClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_simspaceweaver.client import SimSpaceWeaverClient
except ImportError:
    SimSpaceWeaverClient = object  # type: ignore[misc,assignment]


class SimSpaceWeaverService(
    ServiceFactory[SimSpaceWeaverClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "simspaceweaver"
    _SERVICE_PROP = "simspaceweaver"
