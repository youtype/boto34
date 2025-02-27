"""
Wrapper for aioboto3 ApplicationInsights service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_application_insights/)

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
    # Returns type annotated aioboto3 ApplicationInsights client
    application_insights_client = session.application_insights.client()
    application_insights_client: types_aiobotocore_application_insights.client.ApplicationInsightsClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_application_insights.client import ApplicationInsightsClient

from boto34.aioboto3.service_factory import ServiceFactory


class ApplicationInsightsService(ServiceFactory[ApplicationInsightsClient]):
    SERVICE_NAME = "application-insights"
    _SERVICE_PROP = "application_insights"
