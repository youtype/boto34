"""
Wrapper for boto3 Braket service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_braket/)

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
    # Returns type annotated boto3 Braket client
    braket_client = session.braket.client()
    braket_client: types_boto3_braket.client.BraketClient
    ```
"""

from __future__ import annotations

from types_boto3_braket.client import BraketClient

from boto34.boto3.service_factory import ServiceFactory


class BraketService(ServiceFactory[BraketClient]):
    SERVICE_NAME = "braket"
    _SERVICE_PROP = "braket"
