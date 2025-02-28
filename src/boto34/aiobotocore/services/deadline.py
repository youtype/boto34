"""
Wrapper for aiobotocore DeadlineCloud service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_deadline/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_deadline.client import DeadlineCloudClient

from boto34.aiobotocore.service_factory import ServiceFactory


class DeadlineCloudService(ServiceFactory[DeadlineCloudClient]):
    """
    DeadlineCloud service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_deadline/)
    """
