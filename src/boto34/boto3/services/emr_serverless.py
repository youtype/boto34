"""
Wrapper for boto3 EMRServerless service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_emr_serverless/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_emr_serverless.client import EMRServerlessClient

from boto34.boto3.service_factory import ServiceFactory


class EMRServerlessService(ServiceFactory[EMRServerlessClient]):
    """
    EMRServerless service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_emr_serverless/)
    """
