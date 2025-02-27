"""
Wrapper for boto3 EndUserMessagingSocial service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_socialmessaging/)

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
    # Returns type annotated boto3 EndUserMessagingSocial client
    socialmessaging_client = session.socialmessaging.client()
    socialmessaging_client: types_boto3_socialmessaging.client.EndUserMessagingSocialClient
    ```
"""

from __future__ import annotations

from types_boto3_socialmessaging.client import EndUserMessagingSocialClient

from boto34.boto3.service_factory import ServiceFactory


class EndUserMessagingSocialService(ServiceFactory[EndUserMessagingSocialClient]):
    SERVICE_NAME = "socialmessaging"
    _SERVICE_PROP = "socialmessaging"
