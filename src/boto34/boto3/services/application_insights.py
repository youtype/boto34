"""
Wrapper for boto3 ApplicationInsights service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_application_insights/)

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
    # Returns type annotated boto3 ApplicationInsights client
    application_insights_client = session.application_insights.client()
    application_insights_client: types_boto3_application_insights.client.ApplicationInsightsClient
    ```
"""

from __future__ import annotations

from types_boto3_application_insights.client import ApplicationInsightsClient

from boto34.boto3.service_factory import ServiceFactory


class ApplicationInsightsService(ServiceFactory[ApplicationInsightsClient]):
    SERVICE_NAME = "application-insights"
    _SERVICE_PROP = "application_insights"
