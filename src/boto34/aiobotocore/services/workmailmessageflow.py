"""
Wrapper for aiobotocore WorkMailMessageFlow service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workmailmessageflow/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_workmailmessageflow.client import WorkMailMessageFlowClient

from boto34.aiobotocore.service_factory import ServiceFactory


class WorkMailMessageFlowService(ServiceFactory[WorkMailMessageFlowClient]):
    """
    WorkMailMessageFlow service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workmailmessageflow/)
    """
