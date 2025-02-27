"""
Wrapper for boto3 IVS service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ivs/)

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
    # Returns type annotated boto3 IVS client
    ivs_client = session.ivs.client()
    ivs_client: types_boto3_ivs.client.IVSClient
    ```
"""

from __future__ import annotations

from types_boto3_ivs.client import IVSClient

from boto34.boto3.service_factory import ServiceFactory


class IVSService(ServiceFactory[IVSClient]):
    SERVICE_NAME = "ivs"
    _SERVICE_PROP = "ivs"
