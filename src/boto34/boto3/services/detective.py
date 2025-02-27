"""
Wrapper for boto3 Detective service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_detective/)

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
    # Returns type annotated boto3 Detective client
    detective_client = session.detective.client()
    detective_client: types_boto3_detective.client.DetectiveClient
    ```
"""

from __future__ import annotations

from types_boto3_detective.client import DetectiveClient

from boto34.boto3.service_factory import ServiceFactory


class DetectiveService(ServiceFactory[DetectiveClient]):
    SERVICE_NAME = "detective"
    _SERVICE_PROP = "detective"
