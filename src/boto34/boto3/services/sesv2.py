"""
Wrapper for boto3 SESV2 service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sesv2/)

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
    # Returns type annotated boto3 SESV2 client
    sesv2_client = session.sesv2.client()
    sesv2_client: types_boto3_sesv2.client.SESV2Client
    ```
"""

from __future__ import annotations

from types_boto3_sesv2.client import SESV2Client

from boto34.boto3.service_factory import ServiceFactory


class SESV2Service(ServiceFactory[SESV2Client]):
    SERVICE_NAME = "sesv2"
    _SERVICE_PROP = "sesv2"
