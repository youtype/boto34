"""
Wrapper for aiobotocore EMRContainers service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_emr_containers/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_emr_containers.client import EMRContainersClient

from boto34.aiobotocore.service_factory import ServiceFactory


class EMRContainersService(ServiceFactory[EMRContainersClient]):
    """
    EMRContainers service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_emr_containers/)
    """
