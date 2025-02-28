"""
Wrapper for boto3 AppRegistry service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_servicecatalog_appregistry/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_servicecatalog_appregistry.client import AppRegistryClient

from boto34.boto3.service_factory import ServiceFactory


class AppRegistryService(ServiceFactory[AppRegistryClient]):
    """
    AppRegistry service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_servicecatalog_appregistry/)
    """
