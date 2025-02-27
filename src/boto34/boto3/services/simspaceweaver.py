"""
Wrapper for boto3 SimSpaceWeaver service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_simspaceweaver/)

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
    # Returns type annotated boto3 SimSpaceWeaver client
    simspaceweaver_client = session.simspaceweaver.client()
    simspaceweaver_client: types_boto3_simspaceweaver.client.SimSpaceWeaverClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_simspaceweaver.client import SimSpaceWeaverClient
except ImportError:
    SimSpaceWeaverClient = object  # type: ignore[misc,assignment]


class SimSpaceWeaverService(
    ServiceFactory[SimSpaceWeaverClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "simspaceweaver"
    _SERVICE_PROP = "simspaceweaver"
