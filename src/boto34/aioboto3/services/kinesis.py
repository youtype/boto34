"""
Wrapper for aioboto3 Kinesis service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_kinesis/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_kinesis.client import KinesisClient

from boto34.aioboto3.service_factory import ServiceFactory


class KinesisService(ServiceFactory[KinesisClient]):
    """
    Kinesis service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_kinesis/)
    """
