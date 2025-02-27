"""
Wrapper for boto3 Ivschat service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ivschat/)

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
    # Returns type annotated boto3 Ivschat client
    ivschat_client = session.ivschat.client()
    ivschat_client: types_boto3_ivschat.client.IvschatClient
    ```
"""

from __future__ import annotations

from types_boto3_ivschat.client import IvschatClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_ivschat.client import IvschatClient
except ImportError:
    IvschatClient = object  # type: ignore[misc,assignment]


class IvschatService(
    ServiceFactory[IvschatClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "ivschat"
    _SERVICE_PROP = "ivschat"
