"""
Wrapper for boto3 ConnectCases service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_connectcases/)

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
    # Returns type annotated boto3 ConnectCases client
    connectcases_client = session.connectcases.client()
    connectcases_client: types_boto3_connectcases.client.ConnectCasesClient
    ```
"""

from __future__ import annotations

from types_boto3_connectcases.client import ConnectCasesClient

from boto34.boto3.service_factory import ServiceFactory


class ConnectCasesService(ServiceFactory[ConnectCasesClient]):
    SERVICE_NAME = "connectcases"
    _SERVICE_PROP = "connectcases"
