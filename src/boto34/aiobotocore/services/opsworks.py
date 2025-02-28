"""
Wrapper for aiobotocore OpsWorks service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_opsworks.client import OpsWorksClient

from boto34.aiobotocore.service_factory import ServiceFactory


class OpsWorksService(ServiceFactory[OpsWorksClient]):
    """
    OpsWorks service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/)
    """
