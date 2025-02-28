"""
Wrapper for boto3 AppConfigData service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_appconfigdata/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_appconfigdata.client import AppConfigDataClient

from boto34.boto3.service_factory import ServiceFactory


class AppConfigDataService(ServiceFactory[AppConfigDataClient]):
    """
    AppConfigData service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_appconfigdata/)
    """
