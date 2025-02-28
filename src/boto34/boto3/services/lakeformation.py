"""
Wrapper for boto3 LakeFormation service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_lakeformation/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_lakeformation.client import LakeFormationClient

from boto34.boto3.service_factory import ServiceFactory


class LakeFormationService(ServiceFactory[LakeFormationClient]):
    """
    LakeFormation service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_lakeformation/)
    """
