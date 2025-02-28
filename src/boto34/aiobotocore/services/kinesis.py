"""
Wrapper for aiobotocore Kinesis service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesis/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_kinesis.client import KinesisClient

from boto34.aiobotocore.service_factory import ServiceFactory


class KinesisService(ServiceFactory[KinesisClient]):
    """
    Kinesis service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesis/)
    """
