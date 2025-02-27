"""
Wrapper for aioboto3 S3Control service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_s3control/)

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
    # Returns type annotated aioboto3 S3Control client
    s3control_client = session.s3control.client()
    s3control_client: types_aiobotocore_s3control.client.S3ControlClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_s3control.client import S3ControlClient
except ImportError:
    S3ControlClient = object  # type: ignore[misc,assignment]


class S3ControlService(
    ServiceFactory[S3ControlClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "s3control"
    _SERVICE_PROP = "s3control"
