"""
Wrapper for aioboto3 Synthetics service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_synthetics/)

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
    # Returns type annotated aioboto3 Synthetics client
    synthetics_client = session.synthetics.client()
    synthetics_client: types_aiobotocore_synthetics.client.SyntheticsClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_synthetics.client import SyntheticsClient
except ImportError:
    SyntheticsClient = object  # type: ignore[misc,assignment]


class SyntheticsService(
    ServiceFactory[SyntheticsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "synthetics"
    _SERVICE_PROP = "synthetics"
