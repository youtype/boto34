"""
Wrapper for aioboto3 ECR service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_ecr/)

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
    # Returns type annotated aioboto3 ECR client
    ecr_client = session.ecr.client()
    ecr_client: types_aiobotocore_ecr.client.ECRClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_ecr.client import ECRClient
except ImportError:
    ECRClient = object  # type: ignore[misc,assignment]


class ECRService(
    ServiceFactory[ECRClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "ecr"
    _SERVICE_PROP = "ecr"
