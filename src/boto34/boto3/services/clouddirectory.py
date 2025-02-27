"""
Wrapper for boto3 CloudDirectory service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_clouddirectory/)

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
    # Returns type annotated boto3 CloudDirectory client
    clouddirectory_client = session.clouddirectory.client()
    clouddirectory_client: types_boto3_clouddirectory.client.CloudDirectoryClient
    ```
"""

from __future__ import annotations

from types_boto3_clouddirectory.client import CloudDirectoryClient

from boto34.boto3.service_factory import ServiceFactory


class CloudDirectoryService(ServiceFactory[CloudDirectoryClient]):
    SERVICE_NAME = "clouddirectory"
    _SERVICE_PROP = "clouddirectory"
