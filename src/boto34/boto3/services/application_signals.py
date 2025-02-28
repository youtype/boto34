"""
Wrapper for boto3 CloudWatchApplicationSignals service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_application_signals/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_application_signals.client import CloudWatchApplicationSignalsClient

from boto34.boto3.service_factory import ServiceFactory


class CloudWatchApplicationSignalsService(ServiceFactory[CloudWatchApplicationSignalsClient]):
    """
    CloudWatchApplicationSignals service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_application_signals/)
    """
