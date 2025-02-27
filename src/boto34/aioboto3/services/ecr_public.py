"""
Wrapper for aioboto3 ECRPublic service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_ecr_public/)

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
    # Returns type annotated aioboto3 ECRPublic client
    ecr_public_client = session.ecr_public.client()
    ecr_public_client: types_aiobotocore_ecr_public.client.ECRPublicClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_ecr_public.client import ECRPublicClient
except ImportError:
    ECRPublicClient = object  # type: ignore[misc,assignment]


class ECRPublicService(
    ServiceFactory[ECRPublicClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "ecr-public"
    _SERVICE_PROP = "ecr_public"
