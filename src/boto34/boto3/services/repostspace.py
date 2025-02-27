"""
Wrapper for boto3 RePostPrivate service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_repostspace/)

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
    # Returns type annotated boto3 RePostPrivate client
    repostspace_client = session.repostspace.client()
    repostspace_client: types_boto3_repostspace.client.RePostPrivateClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_repostspace.client import RePostPrivateClient
except ImportError:
    RePostPrivateClient = object  # type: ignore[misc,assignment]


class RePostPrivateService(
    ServiceFactory[RePostPrivateClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "repostspace"
    _SERVICE_PROP = "repostspace"
