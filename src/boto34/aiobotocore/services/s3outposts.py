"""
Wrapper for aiobotocore S3Outposts service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3outposts/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_s3outposts.client import S3OutpostsClient

from boto34.aiobotocore.service_factory import ServiceFactory


class S3OutpostsService(ServiceFactory[S3OutpostsClient]):
    """
    S3Outposts service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3outposts/)
    """
