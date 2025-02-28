"""
Wrapper for boto3 RDSDataService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_rds_data/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_rds_data.client import RDSDataServiceClient

from boto34.boto3.service_factory import ServiceFactory


class RDSDataServiceService(ServiceFactory[RDSDataServiceClient]):
    """
    RDSDataService service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_rds_data/)
    """
