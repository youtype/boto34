"""
Wrapper for boto3 Glue service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_glue/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_glue.client import GlueClient

from boto34.boto3.service_factory import ServiceFactory


class GlueService(ServiceFactory[GlueClient]):
    """
    Glue service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_glue/)
    """
