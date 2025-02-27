"""
Wrapper for aioboto3 Omics service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_omics/)

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
    # Returns type annotated aioboto3 Omics client
    omics_client = session.omics.client()
    omics_client: types_aiobotocore_omics.client.OmicsClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_omics.client import OmicsClient
except ImportError:
    OmicsClient = object  # type: ignore[misc,assignment]


class OmicsService(
    ServiceFactory[OmicsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "omics"
    _SERVICE_PROP = "omics"
