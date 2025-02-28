"""
Wrapper for boto3 RedshiftServerless service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_redshift_serverless/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_redshift_serverless.client import RedshiftServerlessClient

from boto34.boto3.service_factory import ServiceFactory


class RedshiftServerlessService(ServiceFactory[RedshiftServerlessClient]):
    """
    RedshiftServerless service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_redshift_serverless/)
    """
