"""
Wrapper for boto3 Kinesis service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kinesis/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_kinesis.client import KinesisClient

from boto34.boto3.service_factory import ServiceFactory


class KinesisService(ServiceFactory[KinesisClient]):
    """
    Kinesis service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kinesis/)
    """
