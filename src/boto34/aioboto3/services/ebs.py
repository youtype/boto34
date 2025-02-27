"""
Wrapper for aioboto3 EBS service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_ebs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 EBS client
    ebs_client = session.ebs.client()
    ebs_client: types_aiobotocore_ebs.client.EBSClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_ebs.client import EBSClient
except ImportError:
    EBSClient = object  # type: ignore[misc,assignment]


class EBSService(
    ServiceFactory[EBSClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "ebs"
    _SERVICE_PROP = "ebs"
