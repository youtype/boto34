"""
Wrapper for boto3 LexModelBuildingService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_lex_models/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_lex_models.client import LexModelBuildingServiceClient

from boto34.boto3.service_factory import ServiceFactory


class LexModelBuildingServiceService(ServiceFactory[LexModelBuildingServiceClient]):
    """
    LexModelBuildingService service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_lex_models/)
    """
