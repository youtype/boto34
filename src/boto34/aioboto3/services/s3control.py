"""
Wrapper for aioboto3 S3Control service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_s3control/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_s3control.client import S3ControlClient

from boto34.aioboto3.service_factory import ServiceFactory


class S3ControlService(ServiceFactory[S3ControlClient]):
    """
    S3Control service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_s3control/)
    """
