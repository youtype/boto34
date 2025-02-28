"""
Wrapper for boto3 S3Control service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_s3control/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_s3control.client import S3ControlClient

from boto34.boto3.service_factory import ServiceFactory


class S3ControlService(ServiceFactory[S3ControlClient]):
    """
    S3Control service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_s3control/)
    """
