"""
Wrapper for boto3 RDS service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_rds/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_rds.client import RDSClient

from boto34.boto3.service_factory import ServiceFactory


class RDSService(ServiceFactory[RDSClient]):
    """
    RDS service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_rds/)
    """
