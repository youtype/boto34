"""
Wrapper for boto3 ComprehendMedical service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_comprehendmedical/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_comprehendmedical.client import ComprehendMedicalClient

from boto34.boto3.service_factory import ServiceFactory


class ComprehendMedicalService(ServiceFactory[ComprehendMedicalClient]):
    """
    ComprehendMedical service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_comprehendmedical/)
    """
