"""
Wrapper for boto3 FreeTier service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_freetier/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_freetier.client import FreeTierClient

from boto34.boto3.service_factory import ServiceFactory


class FreeTierService(ServiceFactory[FreeTierClient]):
    """
    FreeTier service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_freetier/)
    """
