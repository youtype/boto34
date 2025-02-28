"""
Wrapper for boto3 OpsWorks service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_opsworks/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_opsworks.client import OpsWorksClient
from types_boto3_opsworks.service_resource import OpsWorksServiceResource

from boto34.boto3.service_factory import ServiceResourceFactory


class OpsWorksService(ServiceResourceFactory[OpsWorksClient, OpsWorksServiceResource]):
    """
    OpsWorks service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_opsworks/)
    """
