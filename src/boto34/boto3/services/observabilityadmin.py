"""
Wrapper for boto3 CloudWatchObservabilityAdminService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_observabilityadmin/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_observabilityadmin.client import CloudWatchObservabilityAdminServiceClient

from boto34.boto3.service_factory import ServiceFactory


class CloudWatchObservabilityAdminServiceService(
    ServiceFactory[CloudWatchObservabilityAdminServiceClient]
):
    """
    CloudWatchObservabilityAdminService service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_observabilityadmin/)
    """
