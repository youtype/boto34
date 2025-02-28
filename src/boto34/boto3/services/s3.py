"""
Wrapper for boto3 S3 service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_s3/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_s3.client import S3Client
from types_boto3_s3.service_resource import S3ServiceResource

from boto34.boto3.service_factory import ServiceResourceFactory


class S3Service(ServiceResourceFactory[S3Client, S3ServiceResource]):
    """
    S3 service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_s3/)
    """
