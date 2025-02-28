"""
Wrapper for aioboto3 CloudFormation service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_cloudformation/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_cloudformation.client import CloudFormationClient
from types_aiobotocore_cloudformation.service_resource import CloudFormationServiceResource

from boto34.aioboto3.service_factory import ServiceResourceFactory


class CloudFormationService(
    ServiceResourceFactory[CloudFormationClient, CloudFormationServiceResource]
):
    """
    CloudFormation service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_cloudformation/)
    """
