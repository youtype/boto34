"""
Wrapper for boto3 ConnectCases service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_connectcases/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_connectcases.client import ConnectCasesClient

from boto34.boto3.service_factory import ServiceFactory


class ConnectCasesService(ServiceFactory[ConnectCasesClient]):
    """
    ConnectCases service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_connectcases/)
    """
