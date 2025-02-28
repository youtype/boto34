"""
Wrapper for boto3 ConfigService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_config/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_config.client import ConfigServiceClient

from boto34.boto3.service_factory import ServiceFactory


class ConfigServiceService(ServiceFactory[ConfigServiceClient]):
    """
    ConfigService service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_config/)
    """
