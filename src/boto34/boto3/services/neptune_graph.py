"""
Wrapper for boto3 NeptuneGraph service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_neptune_graph/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 NeptuneGraph client
    neptune_graph_client = session.neptune_graph.client()
    neptune_graph_client: types_boto3_neptune_graph.client.NeptuneGraphClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_neptune_graph.client import NeptuneGraphClient
except ImportError:
    NeptuneGraphClient = object  # type: ignore[misc,assignment]


class NeptuneGraphService(
    ServiceFactory[NeptuneGraphClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "neptune-graph"
    _SERVICE_PROP = "neptune_graph"
