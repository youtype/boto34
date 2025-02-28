"""
Wrapper for boto3 Outposts service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_outposts/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_outposts.client import OutpostsClient

from boto34.boto3.service_factory import ServiceFactory


class OutpostsService(ServiceFactory[OutpostsClient]):
    """
    Outposts service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_outposts/)
    """
