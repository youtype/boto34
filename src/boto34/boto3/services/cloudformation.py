"""
Wrapper for boto3 CloudFormation service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cloudformation/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_cloudformation.client import CloudFormationClient
from types_boto3_cloudformation.service_resource import CloudFormationServiceResource

from boto34.boto3.service_factory import ServiceResourceFactory


class CloudFormationService(
    ServiceResourceFactory[CloudFormationClient, CloudFormationServiceResource]
):
    """
    CloudFormation service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cloudformation/)
    """
