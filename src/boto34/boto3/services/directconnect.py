"""
Wrapper for boto3 DirectConnect service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_directconnect/)

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
    # Returns type annotated boto3 DirectConnect client
    directconnect_client = session.directconnect.client()
    directconnect_client: types_boto3_directconnect.client.DirectConnectClient
    ```
"""

from __future__ import annotations

from types_boto3_directconnect.client import DirectConnectClient

from boto34.boto3.service_factory import ServiceFactory


class DirectConnectService(ServiceFactory[DirectConnectClient]):
    SERVICE_NAME = "directconnect"
    _SERVICE_PROP = "directconnect"
