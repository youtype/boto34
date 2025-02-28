"""
Wrapper for aioboto3 LakeFormation service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_lakeformation/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_lakeformation.client import LakeFormationClient

from boto34.aioboto3.service_factory import ServiceFactory


class LakeFormationService(ServiceFactory[LakeFormationClient]):
    """
    LakeFormation service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_lakeformation/)
    """
