"""
Wrapper for aioboto3 ApplicationInsights service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_application_insights/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_application_insights.client import ApplicationInsightsClient

from boto34.aioboto3.service_factory import ServiceFactory


class ApplicationInsightsService(ServiceFactory[ApplicationInsightsClient]):
    """
    ApplicationInsights service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_application_insights/)
    """
