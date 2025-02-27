"""
Wrapper for aiobotocore NeptuneGraph service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/)

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
    # Returns type annotated aiobotocore NeptuneGraph client
    async with session.neptune_graph.create_client() as neptune_graph_client:
        neptune_graph_client: types_aiobotocore_neptune_graph.client.NeptuneGraphClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_neptune_graph.client import NeptuneGraphClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_neptune_graph.client import NeptuneGraphClient
except ImportError:
    NeptuneGraphClient = object  # type: ignore[misc,assignment]


class NeptuneGraphService(
    ServiceFactory[NeptuneGraphClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "neptune-graph"
    _SERVICE_PROP = "neptune_graph"
