"""
Wrapper for aiobotocore EBS service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ebs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore EBS client
    async with session.ebs.create_client() as ebs_client:
        ebs_client: types_aiobotocore_ebs.client.EBSClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_ebs.client import EBSClient
except ImportError:
    EBSClient = object  # type: ignore[misc,assignment]


class EBSService(
    ServiceFactory[EBSClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "ebs"
    _SERVICE_PROP = "ebs"
