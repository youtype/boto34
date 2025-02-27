"""
Wrapper for boto3 AppFabric service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_appfabric/)

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
    # Returns type annotated boto3 AppFabric client
    appfabric_client = session.appfabric.client()
    appfabric_client: types_boto3_appfabric.client.AppFabricClient
    ```
"""

from __future__ import annotations

from types_boto3_appfabric.client import AppFabricClient

from boto34.boto3.service_factory import ServiceFactory


class AppFabricService(ServiceFactory[AppFabricClient]):
    SERVICE_NAME = "appfabric"
    _SERVICE_PROP = "appfabric"
