"""
Wrapper for boto3 QBusiness service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_qbusiness/)

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
    # Returns type annotated boto3 QBusiness client
    qbusiness_client = session.qbusiness.client()
    qbusiness_client: types_boto3_qbusiness.client.QBusinessClient
    ```
"""

from __future__ import annotations

from types_boto3_qbusiness.client import QBusinessClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_qbusiness.client import QBusinessClient
except ImportError:
    QBusinessClient = object  # type: ignore[misc,assignment]


class QBusinessService(
    ServiceFactory[QBusinessClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "qbusiness"
    _SERVICE_PROP = "qbusiness"
