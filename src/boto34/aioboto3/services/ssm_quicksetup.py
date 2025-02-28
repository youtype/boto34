"""
Wrapper for aioboto3 SystemsManagerQuickSetup service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_ssm_quicksetup/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_ssm_quicksetup.client import SystemsManagerQuickSetupClient

from boto34.aioboto3.service_factory import ServiceFactory


class SystemsManagerQuickSetupService(ServiceFactory[SystemsManagerQuickSetupClient]):
    """
    SystemsManagerQuickSetup service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_ssm_quicksetup/)
    """
