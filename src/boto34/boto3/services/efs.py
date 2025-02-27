"""
Wrapper for boto3 EFS service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_efs/)

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
    # Returns type annotated boto3 EFS client
    efs_client = session.efs.client()
    efs_client: types_boto3_efs.client.EFSClient
    ```
"""

from __future__ import annotations

from types_boto3_efs.client import EFSClient

from boto34.boto3.service_factory import ServiceFactory


class EFSService(ServiceFactory[EFSClient]):
    SERVICE_NAME = "efs"
    _SERVICE_PROP = "efs"
