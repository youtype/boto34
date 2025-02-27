"""
Wrapper for boto3 QConnect service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_qconnect/)

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
    # Returns type annotated boto3 QConnect client
    qconnect_client = session.qconnect.client()
    qconnect_client: types_boto3_qconnect.client.QConnectClient
    ```
"""

from __future__ import annotations

from types_boto3_qconnect.client import QConnectClient

from boto34.boto3.service_factory import ServiceFactory


class QConnectService(ServiceFactory[QConnectClient]):
    SERVICE_NAME = "qconnect"
    _SERVICE_PROP = "qconnect"
