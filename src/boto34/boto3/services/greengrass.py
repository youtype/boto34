"""
Wrapper for boto3 Greengrass service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_greengrass/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_greengrass.client import GreengrassClient

from boto34.boto3.service_factory import ServiceFactory


class GreengrassService(ServiceFactory[GreengrassClient]):
    """
    Greengrass service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_greengrass/)
    """
