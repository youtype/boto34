"""
Wrapper for boto3 RedshiftDataAPIService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_redshift_data/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_redshift_data.client import RedshiftDataAPIServiceClient

from boto34.boto3.service_factory import ServiceFactory


class RedshiftDataAPIServiceService(ServiceFactory[RedshiftDataAPIServiceClient]):
    """
    RedshiftDataAPIService service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_redshift_data/)
    """
