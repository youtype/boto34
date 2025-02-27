"""
Wrapper for boto3 SecurityLake service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_securitylake/)

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
    # Returns type annotated boto3 SecurityLake client
    securitylake_client = session.securitylake.client()
    securitylake_client: types_boto3_securitylake.client.SecurityLakeClient
    ```
"""

from __future__ import annotations

from types_boto3_securitylake.client import SecurityLakeClient

from boto34.boto3.service_factory import ServiceFactory


class SecurityLakeService(ServiceFactory[SecurityLakeClient]):
    SERVICE_NAME = "securitylake"
    _SERVICE_PROP = "securitylake"
