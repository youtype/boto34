"""
Wrapper for boto3 CloudWatchApplicationSignals service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_application_signals/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 CloudWatchApplicationSignals client
    application_signals_client = session.application_signals.client()
    application_signals_client: (
        types_boto3_application_signals.client.CloudWatchApplicationSignalsClient
    )
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_application_signals.client import CloudWatchApplicationSignalsClient
except ImportError:
    CloudWatchApplicationSignalsClient = object  # type: ignore[misc,assignment]


class CloudWatchApplicationSignalsService(
    ServiceFactory[CloudWatchApplicationSignalsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "application-signals"
    _SERVICE_PROP = "application_signals"
