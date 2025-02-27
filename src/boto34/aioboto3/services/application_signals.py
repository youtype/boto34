"""
Wrapper for aioboto3 CloudWatchApplicationSignals service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_application_signals/)

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
    # Returns type annotated aioboto3 CloudWatchApplicationSignals client
    application_signals_client = session.application_signals.client()
    application_signals_client: (
        types_aiobotocore_application_signals.client.CloudWatchApplicationSignalsClient
    )
    ```
"""

from __future__ import annotations

from types_aiobotocore_application_signals.client import CloudWatchApplicationSignalsClient

from boto34.aioboto3.service_factory import ServiceFactory


class CloudWatchApplicationSignalsService(ServiceFactory[CloudWatchApplicationSignalsClient]):
    SERVICE_NAME = "application-signals"
    _SERVICE_PROP = "application_signals"
