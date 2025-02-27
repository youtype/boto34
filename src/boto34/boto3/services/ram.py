"""
Wrapper for boto3 RAM service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ram/)

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
    # Returns type annotated boto3 RAM client
    ram_client = session.ram.client()
    ram_client: types_boto3_ram.client.RAMClient
    ```
"""

from __future__ import annotations

from types_boto3_ram.client import RAMClient

from boto34.boto3.service_factory import ServiceFactory


class RAMService(ServiceFactory[RAMClient]):
    SERVICE_NAME = "ram"
    _SERVICE_PROP = "ram"
