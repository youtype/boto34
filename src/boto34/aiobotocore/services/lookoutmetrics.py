"""
Wrapper for aiobotocore LookoutMetrics service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutmetrics/)

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
    # Returns type annotated aiobotocore LookoutMetrics client
    async with session.lookoutmetrics.create_client() as lookoutmetrics_client:
        lookoutmetrics_client: types_aiobotocore_lookoutmetrics.client.LookoutMetricsClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_lookoutmetrics.client import LookoutMetricsClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_lookoutmetrics.client import LookoutMetricsClient
except ImportError:
    LookoutMetricsClient = object  # type: ignore[misc,assignment]


class LookoutMetricsService(
    ServiceFactory[LookoutMetricsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "lookoutmetrics"
    _SERVICE_PROP = "lookoutmetrics"
