"""
Wrapper for aioboto3 WorkMailMessageFlow service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_workmailmessageflow/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_workmailmessageflow.client import WorkMailMessageFlowClient

from boto34.aioboto3.service_factory import ServiceFactory


class WorkMailMessageFlowService(ServiceFactory[WorkMailMessageFlowClient]):
    """
    WorkMailMessageFlow service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_workmailmessageflow/)
    """
