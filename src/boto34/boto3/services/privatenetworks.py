"""
Wrapper for boto3 Private5G service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_privatenetworks/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_privatenetworks.client import Private5GClient

from boto34.boto3.service_factory import ServiceFactory


class Private5GService(ServiceFactory[Private5GClient]):
    """
    Private5G service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_privatenetworks/)
    """
