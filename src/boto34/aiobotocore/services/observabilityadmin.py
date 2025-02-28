"""
Wrapper for aiobotocore CloudWatchObservabilityAdminService service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_observabilityadmin/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_observabilityadmin.client import CloudWatchObservabilityAdminServiceClient

from boto34.aiobotocore.service_factory import ServiceFactory


class CloudWatchObservabilityAdminServiceService(
    ServiceFactory[CloudWatchObservabilityAdminServiceClient]
):
    """
    CloudWatchObservabilityAdminService service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_observabilityadmin/)
    """
