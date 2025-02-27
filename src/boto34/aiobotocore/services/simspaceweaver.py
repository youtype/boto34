"""
Wrapper for aiobotocore SimSpaceWeaver service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_simspaceweaver/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore SimSpaceWeaver client
    async with session.simspaceweaver.create_client() as simspaceweaver_client:
        simspaceweaver_client: types_aiobotocore_simspaceweaver.client.SimSpaceWeaverClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_simspaceweaver.client import SimSpaceWeaverClient
except ImportError:
    SimSpaceWeaverClient = object  # type: ignore[misc,assignment]


class SimSpaceWeaverService(
    ServiceFactory[SimSpaceWeaverClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "simspaceweaver"
    _SERVICE_PROP = "simspaceweaver"
