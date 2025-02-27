"""
Wrapper for aiobotocore ApplicationInsights service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_application_insights/)

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
    # Returns type annotated aiobotocore ApplicationInsights client
    async with session.application_insights.create_client() as application_insights_client:
        application_insights_client: (
            types_aiobotocore_application_insights.client.ApplicationInsightsClient
        )
    ```
"""

from __future__ import annotations

from types_aiobotocore_application_insights.client import ApplicationInsightsClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ApplicationInsightsService(ServiceFactory[ApplicationInsightsClient]):
    SERVICE_NAME = "application-insights"
    _SERVICE_PROP = "application_insights"
