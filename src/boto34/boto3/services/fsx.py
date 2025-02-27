"""
Wrapper for boto3 FSx service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_fsx/)

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
    # Returns type annotated boto3 FSx client
    fsx_client = session.fsx.client()
    fsx_client: types_boto3_fsx.client.FSxClient
    ```
"""

from __future__ import annotations

from types_boto3_fsx.client import FSxClient

from boto34.boto3.service_factory import ServiceFactory


class FSxService(ServiceFactory[FSxClient]):
    SERVICE_NAME = "fsx"
    _SERVICE_PROP = "fsx"
