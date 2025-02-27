"""
Wrapper for aioboto3 WorkMailMessageFlow service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_workmailmessageflow/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 WorkMailMessageFlow client
    workmailmessageflow_client = session.workmailmessageflow.client()
    workmailmessageflow_client: types_aiobotocore_workmailmessageflow.client.WorkMailMessageFlowClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_workmailmessageflow.client import WorkMailMessageFlowClient
except ImportError:
    WorkMailMessageFlowClient = object  # type: ignore[misc,assignment]


class WorkMailMessageFlowService(
    ServiceFactory[WorkMailMessageFlowClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "workmailmessageflow"
    _SERVICE_PROP = "workmailmessageflow"
