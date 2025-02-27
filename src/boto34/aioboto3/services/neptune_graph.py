"""
Wrapper for aioboto3 NeptuneGraph service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_neptune_graph/)

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
    # Returns type annotated aioboto3 NeptuneGraph client
    neptune_graph_client = session.neptune_graph.client()
    neptune_graph_client: types_aiobotocore_neptune_graph.client.NeptuneGraphClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_neptune_graph.client import NeptuneGraphClient

from boto34.aioboto3.service_factory import ServiceFactory


class NeptuneGraphService(ServiceFactory[NeptuneGraphClient]):
    SERVICE_NAME = "neptune-graph"
    _SERVICE_PROP = "neptune_graph"
