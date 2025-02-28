"""
Wrapper for aioboto3 OpsWorks service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_opsworks/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_opsworks.client import OpsWorksClient
from types_aiobotocore_opsworks.service_resource import OpsWorksServiceResource

from boto34.aioboto3.service_factory import ServiceResourceFactory


class OpsWorksService(ServiceResourceFactory[OpsWorksClient, OpsWorksServiceResource]):
    """
    OpsWorks service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_opsworks/)
    """
