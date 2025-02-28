"""
Wrapper for boto3 EMR service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_emr/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_emr.client import EMRClient

from boto34.boto3.service_factory import ServiceFactory


class EMRService(ServiceFactory[EMRClient]):
    """
    EMR service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_emr/)
    """
