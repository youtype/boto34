"""
Wrapper for boto3 CloudWatchLogs service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_logs/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_logs.client import CloudWatchLogsClient

from boto34.boto3.service_factory import ServiceFactory


class CloudWatchLogsService(ServiceFactory[CloudWatchLogsClient]):
    """
    CloudWatchLogs service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_logs/)
    """
