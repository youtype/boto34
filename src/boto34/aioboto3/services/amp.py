"""
Wrapper for aioboto3 PrometheusService service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_amp/)

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
    # Returns type annotated aioboto3 PrometheusService client
    amp_client = session.amp.client()
    amp_client: types_aiobotocore_amp.client.PrometheusServiceClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_amp.client import PrometheusServiceClient
except ImportError:
    PrometheusServiceClient = object  # type: ignore[misc,assignment]


class PrometheusServiceService(
    ServiceFactory[PrometheusServiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "amp"
    _SERVICE_PROP = "amp"
