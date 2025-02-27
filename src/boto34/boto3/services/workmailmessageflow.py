"""
Wrapper for boto3 WorkMailMessageFlow service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_workmailmessageflow/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 WorkMailMessageFlow client
    workmailmessageflow_client = session.workmailmessageflow.client()
    workmailmessageflow_client: types_boto3_workmailmessageflow.client.WorkMailMessageFlowClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_workmailmessageflow.client import WorkMailMessageFlowClient
except ImportError:
    WorkMailMessageFlowClient = object  # type: ignore[misc,assignment]


class WorkMailMessageFlowService(
    ServiceFactory[WorkMailMessageFlowClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "workmailmessageflow"
    _SERVICE_PROP = "workmailmessageflow"
