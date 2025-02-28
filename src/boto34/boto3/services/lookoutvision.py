"""
Wrapper for boto3 LookoutforVision service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_lookoutvision/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_lookoutvision.client import LookoutforVisionClient

from boto34.boto3.service_factory import ServiceFactory


class LookoutforVisionService(ServiceFactory[LookoutforVisionClient]):
    """
    LookoutforVision service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_lookoutvision/)
    """
