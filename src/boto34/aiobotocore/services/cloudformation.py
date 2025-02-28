"""
Wrapper for aiobotocore CloudFormation service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudformation/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_cloudformation.client import CloudFormationClient

from boto34.aiobotocore.service_factory import ServiceFactory


class CloudFormationService(ServiceFactory[CloudFormationClient]):
    """
    CloudFormation service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudformation/)
    """
