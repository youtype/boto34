"""
Wrapper for boto3 Redshift service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_redshift/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_redshift.client import RedshiftClient

from boto34.boto3.service_factory import ServiceFactory


class RedshiftService(ServiceFactory[RedshiftClient]):
    """
    Redshift service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_redshift/)
    """
