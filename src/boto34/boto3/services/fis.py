"""
Wrapper for boto3 FIS service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_fis/)

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
    # Returns type annotated boto3 FIS client
    fis_client = session.fis.client()
    fis_client: types_boto3_fis.client.FISClient
    ```
"""

from __future__ import annotations

from types_boto3_fis.client import FISClient

from boto34.boto3.service_factory import ServiceFactory


class FISService(ServiceFactory[FISClient]):
    SERVICE_NAME = "fis"
    _SERVICE_PROP = "fis"
