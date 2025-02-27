"""
Wrapper for boto3 Shield service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_shield/)

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
    # Returns type annotated boto3 Shield client
    shield_client = session.shield.client()
    shield_client: types_boto3_shield.client.ShieldClient
    ```
"""

from __future__ import annotations

from types_boto3_shield.client import ShieldClient

from boto34.boto3.service_factory import ServiceFactory


class ShieldService(ServiceFactory[ShieldClient]):
    SERVICE_NAME = "shield"
    _SERVICE_PROP = "shield"
