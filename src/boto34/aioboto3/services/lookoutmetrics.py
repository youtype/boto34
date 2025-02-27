"""
Wrapper for aioboto3 LookoutMetrics service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_lookoutmetrics/)

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
    # Returns type annotated aioboto3 LookoutMetrics client
    lookoutmetrics_client = session.lookoutmetrics.client()
    lookoutmetrics_client: types_aiobotocore_lookoutmetrics.client.LookoutMetricsClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_lookoutmetrics.client import LookoutMetricsClient

from boto34.aioboto3.service_factory import ServiceFactory


class LookoutMetricsService(ServiceFactory[LookoutMetricsClient]):
    SERVICE_NAME = "lookoutmetrics"
    _SERVICE_PROP = "lookoutmetrics"
