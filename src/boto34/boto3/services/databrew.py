"""
Wrapper for boto3 GlueDataBrew service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_databrew/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_databrew.client import GlueDataBrewClient

from boto34.boto3.service_factory import ServiceFactory


class GlueDataBrewService(ServiceFactory[GlueDataBrewClient]):
    """
    GlueDataBrew service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_databrew/)
    """
