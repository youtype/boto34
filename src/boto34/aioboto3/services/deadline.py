"""
Wrapper for aioboto3 DeadlineCloud service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_deadline/)

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
    # Returns type annotated aioboto3 DeadlineCloud client
    deadline_client = session.deadline.client()
    deadline_client: types_aiobotocore_deadline.client.DeadlineCloudClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_deadline.client import DeadlineCloudClient
except ImportError:
    DeadlineCloudClient = object  # type: ignore[misc,assignment]


class DeadlineCloudService(
    ServiceFactory[DeadlineCloudClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "deadline"
    _SERVICE_PROP = "deadline"
