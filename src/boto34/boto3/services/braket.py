"""
Wrapper for boto3 Braket service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_braket/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_braket.client import BraketClient

from boto34.boto3.service_factory import ServiceFactory


class BraketService(ServiceFactory[BraketClient]):
    """
    Braket service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_braket/)
    """
