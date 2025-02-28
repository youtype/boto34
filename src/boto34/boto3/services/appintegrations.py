"""
Wrapper for boto3 AppIntegrationsService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_appintegrations/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_appintegrations.client import AppIntegrationsServiceClient

from boto34.boto3.service_factory import ServiceFactory


class AppIntegrationsServiceService(ServiceFactory[AppIntegrationsServiceClient]):
    """
    AppIntegrationsService service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_appintegrations/)
    """
