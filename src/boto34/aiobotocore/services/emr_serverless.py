"""
Wrapper for aiobotocore EMRServerless service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_emr_serverless/)

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
    # Returns type annotated aiobotocore EMRServerless client
    async with session.emr_serverless.create_client() as emr_serverless_client:
        emr_serverless_client: types_aiobotocore_emr_serverless.client.EMRServerlessClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_emr_serverless.client import EMRServerlessClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_emr_serverless.client import EMRServerlessClient
except ImportError:
    EMRServerlessClient = object  # type: ignore[misc,assignment]


class EMRServerlessService(
    ServiceFactory[EMRServerlessClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "emr-serverless"
    _SERVICE_PROP = "emr_serverless"
