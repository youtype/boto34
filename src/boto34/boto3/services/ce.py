"""
Wrapper for boto3 CostExplorer service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ce/)

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
    # Returns type annotated boto3 CostExplorer client
    ce_client = session.ce.client()
    ce_client: types_boto3_ce.client.CostExplorerClient
    ```
"""

from __future__ import annotations

from types_boto3_ce.client import CostExplorerClient

from boto34.boto3.service_factory import ServiceFactory


class CostExplorerService(ServiceFactory[CostExplorerClient]):
    SERVICE_NAME = "ce"
    _SERVICE_PROP = "ce"
