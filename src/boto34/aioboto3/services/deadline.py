"""
Wrapper for aioboto3 DeadlineCloud service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_deadline/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_deadline.client import DeadlineCloudClient

from boto34.aioboto3.service_factory import ServiceFactory


class DeadlineCloudService(ServiceFactory[DeadlineCloudClient]):
    """
    DeadlineCloud service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_deadline/)
    """
