"""
Wrapper for aiobotocore WorkMailMessageFlow service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workmailmessageflow/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore WorkMailMessageFlow client
    async with session.workmailmessageflow.create_client() as workmailmessageflow_client:
        workmailmessageflow_client: (
            types_aiobotocore_workmailmessageflow.client.WorkMailMessageFlowClient
        )
    ```
"""

from __future__ import annotations

from types_aiobotocore_workmailmessageflow.client import WorkMailMessageFlowClient

from boto34.aiobotocore.service_factory import ServiceFactory


class WorkMailMessageFlowService(ServiceFactory[WorkMailMessageFlowClient]):
    SERVICE_NAME = "workmailmessageflow"
    _SERVICE_PROP = "workmailmessageflow"
