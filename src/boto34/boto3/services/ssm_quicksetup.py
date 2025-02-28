"""
Wrapper for boto3 SystemsManagerQuickSetup service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ssm_quicksetup/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_ssm_quicksetup.client import SystemsManagerQuickSetupClient

from boto34.boto3.service_factory import ServiceFactory


class SystemsManagerQuickSetupService(ServiceFactory[SystemsManagerQuickSetupClient]):
    """
    SystemsManagerQuickSetup service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ssm_quicksetup/)
    """
