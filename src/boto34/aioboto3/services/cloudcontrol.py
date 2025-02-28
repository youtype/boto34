"""
Wrapper for aioboto3 CloudControlApi service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_cloudcontrol/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_cloudcontrol.client import CloudControlApiClient

from boto34.aioboto3.service_factory import ServiceFactory


class CloudControlApiService(ServiceFactory[CloudControlApiClient]):
    """
    CloudControlApi service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_cloudcontrol/)
    """
