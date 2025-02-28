"""
Wrapper for boto3 SsmSap service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ssm_sap/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_ssm_sap.client import SsmSapClient

from boto34.boto3.service_factory import ServiceFactory


class SsmSapService(ServiceFactory[SsmSapClient]):
    """
    SsmSap service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ssm_sap/)
    """
