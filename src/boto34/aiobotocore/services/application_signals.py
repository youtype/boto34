"""
Wrapper for aiobotocore CloudWatchApplicationSignals service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_application_signals/)

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
    # Returns type annotated aiobotocore CloudWatchApplicationSignals client
    async with session.application_signals.create_client() as application_signals_client:
        application_signals_client: (
            types_aiobotocore_application_signals.client.CloudWatchApplicationSignalsClient
        )
    ```
"""

from __future__ import annotations

from types_aiobotocore_application_signals.client import CloudWatchApplicationSignalsClient

from boto34.aiobotocore.service_factory import ServiceFactory


class CloudWatchApplicationSignalsService(ServiceFactory[CloudWatchApplicationSignalsClient]):
    SERVICE_NAME = "application-signals"
    _SERVICE_PROP = "application_signals"
