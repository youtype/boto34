"""
Wrapper for boto3 Firehose service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_firehose/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_firehose.client import FirehoseClient

from boto34.boto3.service_factory import ServiceFactory


class FirehoseService(ServiceFactory[FirehoseClient]):
    """
    Firehose service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_firehose/)
    """
