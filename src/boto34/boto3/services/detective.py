"""
Wrapper for boto3 Detective service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_detective/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_detective.client import DetectiveClient

from boto34.boto3.service_factory import ServiceFactory


class DetectiveService(ServiceFactory[DetectiveClient]):
    """
    Detective service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_detective/)
    """
