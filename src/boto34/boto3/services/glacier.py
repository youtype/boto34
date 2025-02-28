"""
Wrapper for boto3 Glacier service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_glacier/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_glacier.client import GlacierClient
from types_boto3_glacier.service_resource import GlacierServiceResource

from boto34.boto3.service_factory import ServiceResourceFactory


class GlacierService(ServiceResourceFactory[GlacierClient, GlacierServiceResource]):
    """
    Glacier service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_glacier/)
    """
