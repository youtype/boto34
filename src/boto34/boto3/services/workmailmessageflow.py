"""
Wrapper for boto3 WorkMailMessageFlow service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_workmailmessageflow/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_workmailmessageflow.client import WorkMailMessageFlowClient

from boto34.boto3.service_factory import ServiceFactory


class WorkMailMessageFlowService(ServiceFactory[WorkMailMessageFlowClient]):
    """
    WorkMailMessageFlow service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_workmailmessageflow/)
    """
