"""
Wrapper for aiobotocore SagemakerEdgeManager service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker_edge/)

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
    # Returns type annotated aiobotocore SagemakerEdgeManager client
    async with session.sagemaker_edge.create_client() as sagemaker_edge_client:
        sagemaker_edge_client: types_aiobotocore_sagemaker_edge.client.SagemakerEdgeManagerClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_sagemaker_edge.client import SagemakerEdgeManagerClient

from boto34.aiobotocore.service_factory import ServiceFactory


class SagemakerEdgeManagerService(ServiceFactory[SagemakerEdgeManagerClient]):
    SERVICE_NAME = "sagemaker-edge"
    _SERVICE_PROP = "sagemaker_edge"
