"""
Wrapper for aioboto3 ComprehendMedical service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_comprehendmedical/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_comprehendmedical.client import ComprehendMedicalClient

from boto34.aioboto3.service_factory import ServiceFactory


class ComprehendMedicalService(ServiceFactory[ComprehendMedicalClient]):
    """
    ComprehendMedical service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_comprehendmedical/)
    """
